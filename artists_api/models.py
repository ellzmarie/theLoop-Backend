from django.db import models

# Create your models here.
class Artist(models.Model):
  name = models.CharField(max_length=100)
  image = models.CharField(max_length=5000)
  release_date = models.CharField(max_length=100)
  description = models.CharField(max_length=1000)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)