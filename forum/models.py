from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    poster_name = models.CharField(max_length=100)
    deceased_name = models.CharField(max_length=100)
    background_story = models.TextField()
    message_to_deceased = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
     
    def preview(self):
        return self.message_to_deceased[:100] + "..."