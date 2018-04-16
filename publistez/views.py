from django.shortcuts import render
from django.utils import timezone
from .models import Article

def post_list(request):
    articles = Article.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'publistez/post_list.html', {'articles': articles})

