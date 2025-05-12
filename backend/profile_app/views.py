from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from db.models import Board

@login_required
def profile(request):
    latest_boards = Board.objects.all()
    print("Boards in DB:", latest_boards)
    print("..............................................")
    print(request.user)
    return render(request, 'profile_app/profile.html', {
        "user": request.user,
        "latest_boards": latest_boards
    })


@login_required
def home_page(request):
    return render(request, "home_app/home.html")

def logout_view(request):
    django_logout(request)
    request.session.flush()  
    return redirect("landing_page") 
