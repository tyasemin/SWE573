from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required

def profile(request):
    return render(request, "profile_app/profile.html")

@login_required
def home_page(request):
    return render(request, "home_app/home.html")

def logout_view(request):
    django_logout(request)
    request.session.flush()  
    return redirect("landing_page") 
