from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from db.models import Board
import random
from django.db.models.functions import Random

def profile(request):
    return render(request, "home_app/home.html")

def logout_view(request):
    django_logout(request)
    request.session.flush()  
    return redirect("landing_page") 

@login_required
def home_page(request):
    boards = Board.objects.all()
    boards = Board.objects.order_by('?')[:10]  # ✅ randomly ordered queryset
    return render(request, "home_app/home.html", {
        "boards": boards
    })

print("🟢 Boards:", Board.objects.all())
print("🎲 Random boards:", Board.objects.order_by('?')[:10])



