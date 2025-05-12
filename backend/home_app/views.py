from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from db.models import Board
import random
from django.db.models.functions import Random
from django.shortcuts import render
from .models import Board

def profile(request):
    return render(request, "home_app/home.html")

def logout_view(request):
    django_logout(request)
    request.session.flush()  
    return redirect("landing_page") 

from django.db import connection

@login_required
def home_page(request):
    boards = Board.objects.all()
    return render(request, "your_template.html", {"boards": boards})


