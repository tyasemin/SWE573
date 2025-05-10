from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile, name="home_page"),
    path('logout/', views.logout_view, name='logout'),
]
