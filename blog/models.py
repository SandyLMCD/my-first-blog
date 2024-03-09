from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

# This defiens our object
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # models.CharField(max_length=xx) is how you define text with a limited number of characters
    title = models.CharField(max_length=200)

    # models.TextField() has no character limit
    text = models.TextField()

    # Date and time
    created_date = models.DateTimeField(default=timezone.now)

    published_date = models.DateTimeField(blank=True, null=True)

    def publish (self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

