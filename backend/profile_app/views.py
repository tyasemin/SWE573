from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout

def profile(request):
    return render(request, "profile_app/profile.html")

def logout_view(request):
    django_logout(request)
    request.session.flush()  
    return redirect("landing_page") 
