from uuid import uuid4

from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone


class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    body = RichTextField()
    photo = models.ImageField(upload_to="blog/%Y/%m/%d/", blank=True)
    schedule = models.DateTimeField(default=None, blank=True, null=True)
    status = models.BooleanField(default=True)
    press_center = models.BooleanField(default=False, verbose_name="Prece Center Page")
    home_page = models.BooleanField(default=False, verbose_name="Home Page")
    date_time = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=timezone.now)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Blogs"


class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    body = models.TextField()
    photo = models.ImageField(upload_to="news/%Y/%m/%d/", blank=True)
    link = models.URLField(max_length=500)
    press_center = models.BooleanField(default=False, verbose_name="Prece Center Page")
    created_at = models.DateTimeField(auto_now_add=timezone.now)
    updated_at = models.DateTimeField(auto_now=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "News"


class Testimonials(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="testimonials/%Y/%m/%d/", blank=True)
    body = models.TextField()
    company = models.CharField(max_length=100, blank=True, null=True)
    youtube_link = models.URLField()
    press_center = models.BooleanField(default=False, verbose_name="Prece Center Page")
    created_at = models.DateTimeField(auto_now_add=timezone.now)
    updated_at = models.DateTimeField(auto_now=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Testimonials"
