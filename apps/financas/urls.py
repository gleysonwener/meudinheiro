from django.urls import path
from . import views

app_name = 'financas'

urlpatterns =[
    path('', views.principal, name='principal'),
]
