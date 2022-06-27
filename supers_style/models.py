from django.db import models

# Create your models here.
class SupersStyle(models.Model):
    type = models.CharField(max_length=255)
    
