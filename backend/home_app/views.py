from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from .models import Board
import random
from django.db.models.functions import Random

def profile(request):
    return render(request, "home_app/home.html")

def logout_view(request):
    django_logout(request)
    request.session.flush()  
    return redirect("landing_page") 

def home_page(request):
    boards = Board.objects.order_by(Random())[:10]
    random.shuffle(boards)  # shuffle in Python memory
    boards = boards[:10]    # take 10

    return render(request, "home_app/home.html", {
        "boards": boards
    })

