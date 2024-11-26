from django.db import models
from taggit.managers import TaggableManager
from django.conf import settings
from tinymce.models import HTMLField

# Create your models here.
class Note(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author', null=True)
    title = models.CharField(max_length=500, blank=False, null=True)
    body = HTMLField(blank=False, null=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title
