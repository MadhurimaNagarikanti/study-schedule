from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
from django import forms
from .models import Customer

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Password input hidden

    class Meta:
        model = Customer
        fields = ['name', 'email', 'password', 'hint_selection', 'hint_answer']
        widgets = {
            'hint_selection': forms.Select(choices=Customer.HINT_CHOICES),  # Dropdown for hint
        }
