from django import forms

from daycare.models import Enrollment, Event, Babysitter


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = [
            'parent_name', 'email', 'phone',
            'child_name', 'gender', 'dob', 'allergies'
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_time', 'end_time', 'location']

class BabysitterForm(forms.ModelForm):
    class Meta:
        model = Babysitter
        fields = '__all__'