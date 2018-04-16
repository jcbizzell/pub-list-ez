from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Article

def pubs_list(request):
    articles = Article.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'publistez/pubs_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'publistez/article_detail.html', {'article': article})

