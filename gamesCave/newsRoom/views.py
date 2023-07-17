from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.contrib.auth.decorators import login_required
from .models import News, Profile, Comments
from .forms import CommentForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.core.exceptions import PermissionDenied


def staff_check(user):
    return user.is_authenticated and user.is_staff

def owner_check(user, comment):
    if user.is_authenticated and (comment.author == user or user.is_staff):
        return True
    return False


# Create your views here.
@login_required
def news_list(request):
    news = News.published.all()
    paginator = Paginator(news, 6)

    page_number = request.GET.get('page')
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

    return render(request, 'news.html', context)  

@login_required
def news_detail(request, slug, id):
    profile = get_object_or_404(Profile, user=request.user)
    news = get_object_or_404(News, slug=slug, id=id)
    comments = news.comments.all().filter(status='published')

    if request.method == 'POST':
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
            return redirect(request.path)
    else:
        comment_form = CommentForm()

    context = {
        'comment_form': comment_form,
        'comments': comments,
        'news': news
    }

    return render(request, 'news_detail.html', context)

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
        return staff_check(self.request.user)
    
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
