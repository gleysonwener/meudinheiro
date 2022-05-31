from django.urls import path
from . import views

app_name = 'financas'

urlpatterns =[
    path('nova_categoria', views.nova_categoria, name='nova_categoria'),
    path('lista_categorias', views.lista_categorias, name='lista_categorias'),
    path('editar_categoria/<int:pk>/', views.editar_categoria, name='editar_categoria'),
    path('apagar_categoria/<int:pk>/', views.apagar_categoria, name='apagar_categoria'),
    path('nova_receita/', views.nova_receita, name='nova_receita'),
    path('lista_receitas/', views.lista_receitas, name='lista_receitas'),
    path('', views.principal, name='principal'),
]
