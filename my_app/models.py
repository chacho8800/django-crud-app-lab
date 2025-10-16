from django.db import models
from django.urls import reverse

# Create your models here.
class NationalParks(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("park-detail", kwargs={"park_id": self.id})
    

