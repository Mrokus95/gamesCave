from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status='published')


class News(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )

    title= models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, default='Anonymous', related_name='news', to_field='nick')
    body = models.TextField()
    image = models.ImageField(upload_to='news/main_images/', blank=False, null=False)
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=9)
    objects = models.Manager()
    published = PublishedManager()
    

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'slug': self.slug, 'id': self.id})
    