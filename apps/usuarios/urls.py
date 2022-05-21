from django.urls import path

app_name = 'usuarios'

from . import views

urlpatterns = [
    path('login/', views.usuario_login, name='usuario_login'),
    path('novo/', views.novo_usuario, name='novo_usuario'),
    path('', views.inicio, name='inicio'),
]
