from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(null=True)
    maximum_retail_price = models.PositiveIntegerField()
    rating = models.FloatField(default=0.0)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return f'{self.title} by {self.author}'

    def get_absolute_url(self):
        # Returns the url to access a particular book instance
        return reverse('book-detail', args=[str(self.id)]) 


class BookCopy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(null=True, blank=True)
    # True status means that the copy is available for issue, False means unavailable
    status = models.BooleanField(default=False)
    borrower = models.ForeignKey(User, related_name='borrower', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        if self.borrow_date:
            return f'{self.book.title}, {str(self.borrow_date)}'
        else:
            return f'{self.book.title} - Available'

class BookRating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rater = models.ForeignKey(User, related_name='rater', null=True, blank=True, on_delete=models.SET_NULL)
    rated = models.BooleanField(default = False)
    rating=models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.book.title} by {self.rater} : {self.rated}'