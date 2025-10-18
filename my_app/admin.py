from django.contrib import admin
from .models import NationalParks, Animal, Activity

# Register your models here.
admin.site.register(NationalParks)
admin.site.register(Animal)
admin.site.register(Activity)
