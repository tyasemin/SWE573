from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from db.models import Board
from .forms import BoardForm

@login_required
def create_board(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.owner = request.user
            board.number_of_nodes = 0
            board.number_of_connections = 0
            board.number_of_contributors = 0  
            board.save()
            return redirect('home_page')
    else:
        form = BoardForm()
    
    return render(request, 'board/create_board.html', {'form': form})

