from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class food(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title