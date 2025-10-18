from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import NationalParks, Animal, Activity
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from .forms import AnimalForm, ActivityForm


# Create your views here.
def home(request):  # home 
    return render(request, 'home.html')

def parks(request): # index 
    parks = NationalParks.objects.all()
    return render(request, 'parks/index.html', {'parks' : parks})

def park_detail(request, park_id): # detail
    park = NationalParks.objects.get(id=park_id)
    activitys = Activity.objects.all()
    animals = park.animals.all()
    animal_form = AnimalForm()
    return render(request, 'parks/detail.html', {
        'park': park,
        'animal_form' : animal_form,
        "animals" : animals,
        'activitys' : activitys
        })

def add_animal(request, park_id): 
    form = AnimalForm(request.POST)

    if form.is_valid():
        new_animal = form.save(commit=False)
        new_animal.park_id = park_id
        new_animal.save()
    return redirect('park-detail', park_id = park_id)


class ParkCreate(CreateView): # create
    model = NationalParks
    fields = ['name','location', 'description']


class ParkUpdate(UpdateView): # update
    model = NationalParks
    fields = ['name','location', 'description']

class ParkDelete(DeleteView): # delete
    model = NationalParks
    success_url = '/parks/'


class ActivityCreate(CreateView):
    model = Activity
    form_class = ActivityForm

class ActivityList(ListView):
    model = Activity

class ActivityDetail(DetailView):
    model = Activity

class ActivityDelete(DeleteView):
    model = Activity
    success_url = '/activity/'

class ActivityUpdate(UpdateView):
    model = Activity
    form_class = ActivityForm
