from django.urls import path
from .views import get_all_robots 

urlpatterns = [
    path('test/', get_all_robots, name='test')
]