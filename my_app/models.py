from django.db import models

# Create your models here.
class NationalParks(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
