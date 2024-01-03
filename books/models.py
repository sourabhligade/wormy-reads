from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='covers/')




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
