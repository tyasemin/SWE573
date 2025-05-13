from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from db.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Kullanıcı Adı')
    password = forms.CharField(widget=forms.PasswordInput, label='Şifre')

class UserRegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    occupation = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'occupation', 'password1', 'password2']
