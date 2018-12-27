from django.db import models

# Create your models here.

class boardDB(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    context = models.TextField()
    create_date = models.DateTimeField(auto_now=True)