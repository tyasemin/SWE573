from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .forms import RegistrationForm, LoginForm
from db.models import User  # kendi User modelini kullanıyorsun

def landing_page(request):
    login_form = LoginForm()
    reg_form = RegistrationForm()

    if request.method == "POST":
        if "login" in request.POST:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]
                try:
                    user = User.objects.get(username=username)
                    if check_password(password, user.password_hash):
                        return redirect("profile")  # profile url tanımlı olmalı
                    else:
                        login_form.add_error(None, "Incorrect password.")
                except User.DoesNotExist:
                    login_form.add_error("username", "User not found.")
        else:
            reg_form = RegistrationForm(request.POST)
            if reg_form.is_valid():
                reg_form.save()
                return redirect("landing_page")

    return render(request, "landing/index.html", {
        "form": reg_form,
        "login_form": login_form,
    })

def profile(request):
    return render(request, "profile/profile.html")  
