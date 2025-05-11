from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .forms import RegistrationForm, LoginForm
from db.models import User  

from django.contrib.auth import authenticate, login

def landing_page(request):
    ...
    if request.method == 'POST' and "login" in request.POST:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # ✅ This sets request.user!
                return redirect('profile')
            else:
                login_form.add_error(None, "Invalid credentials")


from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile(request):
    return render(request, "profile_app/profile.html", {"user": request.user})

