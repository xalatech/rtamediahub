from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models import Count, Case, When, IntegerField
from rta import settings
import os
from .validators import validate_file_extension


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=700, null=True)
    icon = models.CharField(max_length=255)
    widgetColor = models.CharField(max_length=255)
    sortOrder = models.IntegerField()
    createdOn = models.DateTimeField(auto_now_add=True)
    creeatedBy = models.ForeignKey(User,
                                   null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Post(models.Model):
    headline = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=100, null=True, blank=True)
    tags = models.CharField(max_length=255, null=True, blank=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name='%(class)s_requests_created')
    updatedOn = models.DateTimeField(auto_now_add=True)
    updatedBy = models.ForeignKey(User,
                                  null=True, blank=True, on_delete=models.SET_NULL, related_name='%(class)s_requests_updated')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    upload = models.FileField(upload_to='%Y/%m/%d/', null=True,
                              blank=True, validators=[validate_file_extension])
    thumb = models.CharField(
        max_length=255, default='media/thumbs/default.png', blank=True)

    def __str__(self):
        return self.headline

    def filename(self):
        return os.path.join("media/", self.upload.name)

    def update_thumb(self, thumb):
        self.thumb = thumb
        self.save()
