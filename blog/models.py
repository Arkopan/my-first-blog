from django.db import models
from django.conf import settings
from django.db.models.query import QuerySet
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status='published')

class Post(models.Model):

    class PublishingState(models.TextChoices):
        DRAFT = 'draft', _('Draft')
        PUBLISHED = 'published', _('Published')

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='published_date')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=PublishingState.choices, default=PublishingState.DRAFT)

    objects = models.Manager() # менеджер по умолчанию
    published = PublishedManager() # новый менеджер

    class Meta:
        ordering = ('-published_date',)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.published_date.year,self.published_date.month,self.published_date.day,self.slug])

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    
    def __str__(self):
        return self.title
    