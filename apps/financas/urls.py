from django.urls import path
from . import views

app_name = 'financas'

urlpatterns =[
    path('nova_categoria', views.nova_categoria, name='nova_categoria'),
    path('lista_categorias', views.lista_categorias, name='lista_categorias'),
    path('', views.principal, name='principal'),
]
