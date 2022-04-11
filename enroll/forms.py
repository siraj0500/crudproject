# (5) creating forms.py and forms inside to create the contents for the form
# import forms from django and from models import User

from django import forms
from .models import User


# creating class for models and the class inherit from forms.ModelForm

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User # inherit from models.py
        fields = ['name', 'email', 'password'] # creating fields to specify
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
            # render value=True to make the password visible in editing process (by dots)
        }
