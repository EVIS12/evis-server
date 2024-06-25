from uuid import uuid4

from ckeditor.fields import RichTextField
from django.db import models


class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    body = RichTextField()
    photo = models.ImageField(upload_to="blog/%Y/%m/%d/", blank=True)
    schedule = models.DateTimeField(default=None, blank=True, null=True)
    status = models.BooleanField(default=True)
    press_center = models.BooleanField(default=False, verbose_name="Prece Center Page")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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
    link = models.URLField()
    press_center = models.BooleanField(default=False, verbose_name="Prece Center Page")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
    youtube_link = models.URLField()
    press_center = models.BooleanField(default=False, verbose_name="Prece Center Page")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Testimonials"
