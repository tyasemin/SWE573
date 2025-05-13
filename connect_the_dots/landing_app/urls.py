from django.urls import path
from .views import landing_page
from .views import profile

urlpatterns = [
    path('', landing_page, name='landing'),
    path('profile/', profile, name='profile'),
]