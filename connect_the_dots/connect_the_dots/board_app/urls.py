from django.urls import path
from .views import board_detail
from . import views

urlpatterns = [
    path('<int:board_id>/', board_detail, name='board_detail'),
    path('add-node/', views.add_node, name='add_node')
]