from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Genre(models.Model):
    GENRE_CHOICES = [
        ('FICTION', 'Fiction'),
        ('NON-FICTION', 'Non-Fiction'),
        ('AUTOBIOGRAPHY', 'Autobiography'),
        ('NOVELS', 'Novels'),
        ('THRILLERS', 'Thrillers'),
        ('HISTORY', 'History'),
        ('POETRY', 'Poetry'),
    ]

    name = models.CharField(max_length=20, choices=GENRE_CHOICES)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='covers/')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)



    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)  # Assuming a simple user field for demonstration
    text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    rating = models.PositiveIntegerField(default=0)  # Default value added here
    comment = models.TextField()
    comment = models.CharField(max_length=200, default='')

    def __str__(self):
        return f"Review for {self.book.title} by {self.user}"
    


