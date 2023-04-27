from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.ManyToManyField(User, related_name='related_post', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["-created_at"]


class Connection(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name='following', blank=True)

    def __str__(self):
        return self.user.screen_name