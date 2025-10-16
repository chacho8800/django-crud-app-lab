from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import NationalParks, Animal
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import AnimalForm


# Create your views here.
def home(request):  # home 
    return render(request, 'home.html')

def parks(request): # index 
    parks = NationalParks.objects.all()
    return render(request, 'parks/index.html', {'parks' : parks})

def park_detail(request, park_id): # detail
    park = NationalParks.objects.get(id=park_id)
    animals = park.animals.all()
    animal_form = AnimalForm()
    return render(request, 'parks/detail.html', {'park': park, 'animal_form' : animal_form, "animals" : animals} )

def add_animal(request, park_id):
    form = AnimalForm(request.POST)

    if form.is_valid():
        new_animal = form.save(commit=False)
        new_animal.park_id = park_id
        new_animal.save()
    return redirect('park-detail', park_id = park_id)

class ParkCreate(CreateView): # create
    model = NationalParks
    fields = '__all__'


class ParkUpdate(UpdateView): # update
    model = NationalParks, Animal
    fields = '__all__'

class ParkDelete(DeleteView): # delete
    model = NationalParks
    success_url = '/parks/'

