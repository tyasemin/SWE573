from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout

def profile(request):
    return render(request, "home_app/home.html")

def logout_view(request):
    django_logout(request)
    request.session.flush()  
    return redirect("landing_page") 

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Board  # adjust based on your actual model import

@login_required
def home_page(request):
    user_boards = Board.objects.filter(user=request.user)
    return render(request, "home_app/home.html", {"boards": user_boards})
