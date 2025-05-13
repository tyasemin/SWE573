from django.urls import path
from .views import create_board, home_page

urlpatterns = [
    path('', home_page, name='home'),
    path('board/create/', create_board, name='create_board'),
]
