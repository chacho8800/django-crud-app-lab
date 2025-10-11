from django.shortcuts import render
from django.http import HttpResponse
from .models import NationalParks

# Create your views here.
def home(request):  # home 
    return render(request, 'home.html')

def parks(request): # index 
    parks = NationalParks.objects.all()
    return render(request, 'parks/index.html', {'parks' : parks})

def park_detail(request, park_id):
    park = NationalParks.objects.get(id=park_id)
    return render(request, 'parks/detail.html', {'park': park} )
