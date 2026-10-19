from django.db import models
from django.core.exceptions import ValidationError
class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    birth_date = models.DateField()
def __str__(self):
    return self.name
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
def __str__(self):
    return self.name
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=13, unique=True)
    description = models.TextField()
    published_date = models.DateField()
    available_copies = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
def clean(self):
    if self.available_copies < 0:
        raise ValidationError("Available copies cannot be negative.")

def save(self, *args, **kwargs):
    self.full_clean()
    super().save(*args, **kwargs)

def __str__(self):
    return self.title