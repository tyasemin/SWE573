from django import forms
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from db.models import User
import pycountry

# Dropdown için ülke listesi
COUNTRY_CHOICES = sorted([(country.name, country.name) for country in pycountry.countries])
COUNTRY_CHOICES.insert(0, ("", "Select Country"))  

class RegistrationForm(forms.ModelForm):
    location = forms.ChoiceField(choices=COUNTRY_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'password_hash', 'email', 'full_name', 'location', 'occupation']
        widgets = {
            'password_hash': forms.PasswordInput(attrs={'placeholder': 'Password'})
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password_hash = make_password(self.cleaned_data["password_hash"])
        user.registration_date = timezone.now()
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
