from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])

# Create your models here.
