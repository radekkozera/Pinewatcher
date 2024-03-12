from django.urls import path
from .views import create_company, get_all_companies

urlpatterns = [
    path('create-company/', create_company, name='create-company'),
    path('companies/', get_all_companies, name='get-all-companies' )
]
