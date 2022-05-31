from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    role = models.CharField(max_length=20, choices=UserRole.choices, default=UserRole.USER)
    # Возможно нужно добавить еще одно поле, пока не понятно!

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name

