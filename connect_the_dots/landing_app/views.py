from django.shortcuts import render,redirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from db.models import Board

def home(request):
    return render(request, 'landing_app/home.html')

from .forms import UserRegistrationForm

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Başarılı kayıt sonrası yönlendirme
    else:
        form = UserRegistrationForm()

    return render(request, 'landing_app/register.html', {'form': form})


@login_required
def profile(request):
    boards = Board.objects.filter(owner=request.user)
    return render(request, 'landing_app/profile.html', {
        'user': request.user,
        'boards': boards
    })

def landing_page(request):
    login_form = UserLoginForm(request, data=request.POST or None, prefix='login')
    register_form = UserRegistrationForm(request.POST or None, prefix='register')

    if request.method == "POST":
        if 'login-submit' in request.POST and login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('profile')

        elif 'register-submit' in request.POST and register_form.is_valid():
            user = register_form.save()
            login(request, user)
            return redirect('home')

    return render(request, 'landing_app/landing.html', {
        'login_form': login_form,
        'register_form': register_form
    })

