from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from db.forms import BoardForm
from db.models import Board

@login_required
def create_board(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.owner = request.user  # 👈 kullanıcıya ait yap
            board.save()
            return redirect('home')  # oluşturduktan sonra ana sayfaya yönlendir
    else:
        form = BoardForm()

    return render(request, 'home_app/create_board.html', {'form': form})


@login_required
def home_page(request):
    boards = Board.objects.all()
    return render(request, 'home_app/home.html', {
        'boards': boards
    })
