from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    genre_text = models.CharField(max_length=200)

    def __str__(self):
        return self.genre_text

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.IntegerField()
    genre = models.ForeignKey( Genre , on_delete=models.CASCADE )
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Borrow(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    book = models.ForeignKey(Book , on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.name}"


    
