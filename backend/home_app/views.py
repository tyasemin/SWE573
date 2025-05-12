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

from django.db import connection

@login_required
def home_page():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Board")
        results = cursor.fetchall()
    return results


