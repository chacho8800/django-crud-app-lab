from django import forms
from .models import Animal, Activity

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['species', 'count'] 


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }