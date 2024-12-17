from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    """ Caterory model """
    name = models.CharField(max_length=30, unique=True)
    restricted = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("forum:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    """ Subcategory model"""
    name = models.CharField(max_length=30, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("forum:subcategory_detail", kwargs={"pk": self.pk})


class Post(models.Model):
    subject = models.CharField(max_length=60)
    author = models.ForeignKey(
        "user.User", null=True, blank=True, on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(max_length=1000)
    create_date = models.DateTimeField(default=timezone.now)
    upload_file = models.FileField(upload_to="uploads/", blank=True)

    def get_absolute_url(self):
        return reverse("forum:post_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.subject


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=50, null=True, blank=True)
    auth_author = models.ForeignKey(
        "user.User", null=True, blank=True, on_delete=models.CASCADE
    )
    email = models.EmailField(null=True, blank=True)
    text = models.TextField(max_length=1000)
    create_date = models.DateTimeField(default=timezone.now)
    upload_file = models.FileField(upload_to="uploads/", blank=True)

    def __str__(self):
        return self.text
