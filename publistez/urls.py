from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.pubs_list, name='pubs_list'),
    url(r'^article/(?P<pk>\d+)/$', views.article_detail, name='article_detail'),
    url(r'^article/new/$', views.article_new, name='article_new'),
    url(r'^article/(?P<pk>\d+)/edit/$', views.article_edit, name='article_edit'),
]
