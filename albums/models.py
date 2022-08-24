from django.conf import settings
from django.db import models
from django.utils import timezone


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
