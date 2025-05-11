from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Board
from .forms import BoardForm

@login_required
def create_board(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.owner = request.user  # ✅ FIXED this line
            board.save()
            return redirect('home_page')
    else:
        form = BoardForm()
    
    return render(request, 'board/create_board.html', {'form': form})

