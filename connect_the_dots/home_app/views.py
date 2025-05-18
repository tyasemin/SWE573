from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from db.forms import BoardForm
from db.models import Board, Node
from db.models import Activity  
from django.utils import timezone
from django.db.models import Q

@login_required
def create_board(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.owner = request.user  
            board.save()

            return redirect('home')  
    else:
        form = BoardForm()

    return render(request, 'home_app/create_board.html', {'form': form})


@login_required
def home_page(request):
    query = request.GET.get('q', '')
    
    if query:
        boards = Board.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(nodes__title__icontains=query) 
        ).distinct()
    else:
        boards = Board.objects.all().order_by('-created_at')

    return render(request, 'home_app/home.html', {
        'boards': boards,
        'query': query
    })
