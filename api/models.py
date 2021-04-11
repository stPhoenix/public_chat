from django.db import models

# Create your models here.

class Message(models.Model):
    author = models.EmailField()
    text = models.CharField(max_length=100)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    
