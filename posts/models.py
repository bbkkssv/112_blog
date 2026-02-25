from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Status(models.Model):
    class Meta:
        verbose_name_plural = "Status"
        
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256, help_text= "Write a description of the status")

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=128)
    sub_title = models.CharField(max_length=256)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])
    

