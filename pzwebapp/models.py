from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Korisnik(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username


class Exchange(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class LanguageExchange(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    participants = models.ManyToManyField(User, related_name='exchanges')
    language_offered = models.CharField(max_length=50)
    language_requested = models.CharField(max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('exchange_detail', args=[str(self.id)])
