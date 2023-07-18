from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.contrib.auth.decorators import login_required
from .models import News, Profile, Comments
from .forms import CommentForm
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView, BaseUpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.core.exceptions import PermissionDenied



def staff_check(user):
    return user.is_authenticated and user.is_staff

def owner_check(user, comment):
    if user.is_authenticated and (comment.author == user.profile or user.is_staff):
        return True
    return False

def not_owner_check(user, comment):
    if user.is_authenticated and (comment.author != user.profile or user.is_staff):
        return True
    return False



class NewsListView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):

        news = News.published.all()
        paginator = Paginator(news, 6)

        page_number = self.request.GET.get('page')
        try:
            news = paginator.page(page_number)
        except PageNotAnInteger:
            news = paginator.page(1)
        except EmptyPage:
            news = paginator.page(paginator.num_pages)

        context = {
            'news': news,
            'num_pages': paginator.num_pages
        }

        return render(self.request, 'news.html', context)  

    
class NewsDetailView(LoginRequiredMixin, View):
    
    def get(self, request, slug, id):
        news = get_object_or_404(News, slug=slug, id=id)
        comments = news.comments.all()
        comment_form = CommentForm()
        paginator = Paginator(comments, 5)
        page_number = request.GET.get('page')

        try:
            paginated_comments = paginator.page(page_number)
        except PageNotAnInteger:
            paginated_comments = paginator.page(1)
        except EmptyPage:
            paginated_comments = paginator.page(paginator.num_pages)

        context = {
            'comment_form': comment_form,
            'comments': paginated_comments,  # Użyj zmiennej paginated_comments
            'news': news,
            'num_pages': paginator.num_pages
        }

        return render(request, 'news_detail.html', context)
    
    def post(self, request, slug, id):

        profile = get_object_or_404(Profile, user=request.user)
        news = get_object_or_404(News, slug=slug, id=id)
        comments = news.comments.all()

        comment_body = request.POST.get('body')
        comment_form = CommentForm(request.POST)
            
        if len(comment_body) > 500:
            messages.add_message(request, messages.ERROR, "Komentarz przekroczył maksymalną długość")
            comment_form = CommentForm()
                
            return redirect(request.path)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = profile
            new_comment.news = news
            new_comment.save()
            messages.success(request, "Komentarz został dodany pomyślnie.")
            return redirect(request.path)


class NewsCreateView(UserPassesTestMixin, CreateView):
    model = News
    fields = ["title", "body", "image"]

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)
    
    def test_func(self):
        return staff_check(self.request.user)

    def handle_no_permission(self):
        raise PermissionDenied()

class NewsUpdateView(UserPassesTestMixin, UpdateView):
    model = News
    fields = ["title", "body", "image"]
    template_name = 'update_news.html'
    
    def test_func(self):
        return staff_check(self.request.user)
    
    def handle_no_permission(self):
        raise PermissionDenied()

class NewsDeleteView(UserPassesTestMixin, DeleteView):
    model = News
    template_name = 'delete_news_confirmation.html'
    success_url = reverse_lazy('news')  

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    def test_func(self):
        comment = self.get_object()
        return owner_check(self.request.user, comment)
    
    def handle_no_permission(self):
        raise PermissionDenied()


class CommentUpdateView(UserPassesTestMixin, UpdateView):
    model = Comments
    fields = ["body"]


    def test_func(self):
        comment = self.get_object()
        return owner_check(self.request.user, comment)
    
    def get_success_url(self):
        return reverse_lazy('news_detail', kwargs={'slug': self.object.news.slug, 'id': self.object.news.id})

    def handle_no_permission(self):
        raise PermissionDenied()
    
    def form_valid(self, form):
        messages.success(self.request, "Komentarz został zaktualizowany pomyślnie.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Komentarz jest za długi.")
        return super().form_invalid(form)

class CommentDeleteView(UserPassesTestMixin, DeleteView):
    model = Comments


    def get_success_url(self):
        return reverse_lazy('news_detail', kwargs={'slug': self.object.news.slug, 'id': self.object.news.id})
    
    
    def form_valid(self, form):
        messages.success(self.request, "Komentarz został usunięty.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Komentarz nie został usunięty.")
        return super().form_invalid(form)
    
    def test_func(self):
        comment = self.get_object()
        return owner_check(self.request.user, comment)
    
    def handle_no_permission(self):
        raise PermissionDenied()
    

class CommentReportView(UserPassesTestMixin, View):
     
    def post(self, request, pk):
        obj = get_object_or_404(Comments, pk=pk)
        obj.status = "reported"
        obj.save() 
        news_url = reverse_lazy('news_detail', kwargs={'slug': obj.news.slug, 'id': obj.news.id})
        return redirect(news_url)
    
    def handle_no_permission(self):
        raise PermissionDenied()
    
    def test_func(self):
        pk = self.kwargs.get('pk')
        comment = get_object_or_404(Comments, pk=pk)
        return not_owner_check(self.request.user, comment)
    