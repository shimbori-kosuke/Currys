from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class Shop(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        null=True,
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('reviews:shopDetail', kwargs={'pk': self.pk})

class Point(models.Model):
    point = models.IntegerField()
    stars = models.CharField(max_length=255)

    def __str__(self):
        return self.stars

class Review(models.Model):
    name = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
    )
    menu = models.CharField(max_length=255)
    memo = models.TextField()

    ovrpoint = models.ForeignKey(
        Point,
        on_delete=models.PROTECT,
        related_name = 'ovrpoint',
    )
    curpoint = models.ForeignKey(
        Point,
        on_delete=models.PROTECT,
        related_name = 'curpoint',
    )
    naapoint = models.ForeignKey(
        Point,
        on_delete=models.PROTECT,
        related_name = 'naapoint',
    )
    serpoint = models.ForeignKey(
        Point,
        on_delete=models.PROTECT,
        related_name = 'serpoint',
    )
    intpoint = models.ForeignKey(
        Point,
        on_delete=models.PROTECT,
        related_name = 'intpoint',
    )
    toipoint = models.ForeignKey(
        Point,
        on_delete=models.PROTECT,
        related_name = 'toipoint',
    )
    price = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
       ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse('reviews:reviewDetail', kwargs={'pk': self.pk})