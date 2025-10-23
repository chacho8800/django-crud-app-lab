from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import NationalParks, Animal, Activity
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from .forms import AnimalForm, ActivityForm

from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Home(LoginView):  # home 
    template_name = 'home.html'


def signup(request):
    error_message = ''
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('parks-index')
        else : 
            error_message = "Invalid sign up"
    
    form = UserCreationForm()
    context = {'form': form, "error_message" : error_message}
    return render(request, 'signup.html', context)
        
@login_required
def parks(request): # index 
    parks = NationalParks.objects.filter(user=request.user)
    return render(request, 'parks/index.html', {'parks' : parks})

@login_required
def park_detail(request, park_id): # detail
    park = NationalParks.objects.get(id=park_id)
    activitys = Activity.objects.exclude(id__in = park.activity.all().values_list('id'))
    animals = park.animals.all()
    animal_form = AnimalForm()
    return render(request, 'parks/detail.html', {
        'park': park,
        'animal_form' : animal_form,
        "animals" : animals,
        'activitys' : activitys
        })

@login_required
def add_animal(request, park_id): 
    form = AnimalForm(request.POST)

    if form.is_valid():
        new_animal = form.save(commit=False)
        new_animal.park_id = park_id
        new_animal.save()
    return redirect('park-detail', park_id = park_id)

@login_required
def animal_detail(request,animal_id):
    animal_id = Animal.objects.get(id=animal_id)

    print(animal_id)
    return render(request, 'animal/animal_detail.html', {
         'animal': animal_id
        })

@login_required
def add_activity_to_park(request, park_id, activity_id):
    # NationalParks.objects.get(id=park_id).activity.add(id=activity_id)
    park = get_object_or_404(NationalParks, id=park_id)
    activity = get_object_or_404(Activity, id=activity_id)

    park.activity.add(activity)
    return redirect('park-detail', park_id=park_id)


class AnimalsList(LoginRequiredMixin, ListView):
    model = Animal


class AnimalDelete(LoginRequiredMixin, DeleteView):
    model = Animal
    success_url = '/animals/'


class AnimalUpdate(LoginRequiredMixin, UpdateView):
    model = Animal
    form_class = AnimalForm


class ParkCreate(LoginRequiredMixin, CreateView): # create
    model = NationalParks
    fields = ['name','location', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class ParkUpdate(LoginRequiredMixin, UpdateView): # update
    model = NationalParks
    fields = ['name','location', 'description']


class ParkDelete(LoginRequiredMixin, DeleteView): # delete
    model = NationalParks
    success_url = '/parks/'


class ActivityCreate(LoginRequiredMixin, CreateView):
    model = Activity
    form_class = ActivityForm


class ActivityList(LoginRequiredMixin, ListView):
    model = Activity


class ActivityDetail(LoginRequiredMixin, DetailView):
    model = Activity


class ActivityDelete(LoginRequiredMixin, DeleteView):
    model = Activity
    success_url = '/activity/'


class ActivityUpdate(LoginRequiredMixin, UpdateView):
    model = Activity
    form_class = ActivityForm


