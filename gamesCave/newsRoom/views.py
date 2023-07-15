from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from .models import News

# Create your views here.
def news_list(request):
    news = News.published.all()
    paginator = Paginator(news, 2)

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

def news_detail(request, slug, id):
    context = {
    'news' : get_object_or_404(News, slug=slug, id=id)
    }
    return render(request, 'news_detail.html', context)