# Aqui se encontra as funções que executam as páginas
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UsuarioForm


def inicio(request):
    return render(request, 'base.html', {})


def novousuario(request):
    template_name = 'usuarios/novo_usuario.html'
    context = {}

    if request.method == 'POST'
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            messages.success(request, 'Contra criada com sucesso')
            return redirect('usuarios:login_usuario')
    else:
        form = UsuarioForm()
    context['form'] = form
    return render(request, template_name, context)
