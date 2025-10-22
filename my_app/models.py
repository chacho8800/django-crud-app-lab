from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("activity-detail", kwargs={"pk": self.id})
    

class NationalParks(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    activity = models.ManyToManyField(Activity)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("park-detail", kwargs={"park_id": self.id})
    

class Animal(models.Model):
    species = models.CharField(max_length=200)
    count = models.IntegerField()

    park = models.ForeignKey(NationalParks, on_delete=models.CASCADE, related_name='animals')

    def __str__(self):
        return f"{self.species} {self.park.name}"
    
    def get_absolute_url(self):
        return reverse("animal-detail", kwargs={"animal_id": self.id})
        

