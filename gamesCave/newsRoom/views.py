from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.contrib.auth.decorators import login_required
from .models import News
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin


def staff_check(user):
    return user.is_authenticated and user.is_staff

# Create your views here.
@login_required
def news_list(request):
    news = News.published.all()
    paginator = Paginator(news, 3)

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
    context = {
    'news' : get_object_or_404(News, slug=slug, id=id)
    }
    return render(request, 'news_detail.html', context)

class NewsCreateView(UserPassesTestMixin, CreateView):
    model = News
    fields = ["title", "body", "image"]

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)\
    
    def test_func(self):
        return staff_check(self.request.user)

class NewsUpdateView(UserPassesTestMixin, UpdateView):
    model = News
    fields = ["title", "body", "image"]
    template_name = 'update_news.html'
    
    def test_func(self):
        return staff_check(self.request.user)

class NewsDeleteView(UserPassesTestMixin, DeleteView):
    model = News
    template_name = 'delete_news_confirmation.html'
    success_url = reverse_lazy('news')  

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    def test_func(self):
        return staff_check(self.request.user)