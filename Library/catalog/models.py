from django.db import models

class Genre(models.Model):
    genre_text = models.CharField(max_length=200)

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.IntegerField()
    genre = models.ForeignKey( Genre , on_delete=models.CASCADE )



    
