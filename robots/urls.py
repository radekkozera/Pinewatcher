from django.urls import path
from .views import get_all_robots 

urlpatterns = [
    path('robots/', get_all_robots, name='robots')
]