from django.urls import path
from .views import board_detail
from . import views

urlpatterns = [
    path('<int:board_id>/', board_detail, name='board_detail'),
    path('add-node/', views.add_node, name='add_node'),
    path('boards/add-connection/', views.add_connection, name='add_connection'),
    path('delete_node/', views.delete_node, name='delete_node'),
    path('delete_connection/', views.delete_connection, name='delete_connection'),
    path('update-node/', views.update_node, name='update_node'),
]