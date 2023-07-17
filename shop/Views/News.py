from django.shortcuts import render, get_object_or_404
from ..models import News

def index(request):
    all_news = News.objects.all()
    return render(request, 'Pages/blog.html', {'all_news': all_news})

def one_news(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'Pages/blog-details.html', {'news': news})