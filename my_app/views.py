from django.shortcuts import render
from django.http import HttpResponse
from .models import NationalParks
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):  # home 
    return render(request, 'home.html')

def parks(request): # index 
    parks = NationalParks.objects.all()
    return render(request, 'parks/index.html', {'parks' : parks})

def park_detail(request, park_id): # detail
    park = NationalParks.objects.get(id=park_id)
    return render(request, 'parks/detail.html', {'park': park} )

class ParkCreate(CreateView): # create
    model = NationalParks
    fields = '__all__'


class ParkUpdate(UpdateView): # update
    model = NationalParks
    fields = '__all__'

class ParkDelete(DeleteView): # delete
    model = NationalParks
    success_url = '/parks/'