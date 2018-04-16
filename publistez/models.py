from django.db import models
from django.utils import timezone


class Article(models.Model):
    addedby = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.TextField()
    added_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    journal = models.CharField(max_length=200, default='')
    author_str = models.TextField(default='')
    other_str = models.TextField(blank=True, null=True, default='')
    citedby = models.PositiveIntegerField(blank=True, null=True, default=0)
    year = models.PositiveSmallIntegerField(default=0)
    doi = models.CharField(max_length=200, blank=True, null=True, default='')
    pubmed = models.CharField(max_length=200, blank=True, null=True, default='')
    keyword_str = models.TextField(blank=True, null=True, default='')

    #published_date = models.DateTimeField(
    #        blank=True, null=True)

    def save_to_db(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class ArticleListItem(models.Model):
    addedby = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.TextField(default='')
    added_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    journal = models.CharField(max_length=200, default='')
    author_str = models.TextField(default='')
    other_str = models.TextField(blank=True, null=True, default='')
    citedby = models.PositiveIntegerField(blank=True, null=True, default=0)
    year = models.PositiveSmallIntegerField(default=0)
    doi = models.CharField(max_length=200, blank=True, null=True, default='')
    pubmed = models.CharField(max_length=200, blank=True, null=True, default='')
    keyword_str = models.TextField(blank=True, null=True, default='')
    add2db = models.BooleanField(default=True)

    def save_to_db(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title