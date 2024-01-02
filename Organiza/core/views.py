from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tarea, CategoriaTarea
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")

def logout_view(request):
    logout(request)
    redirect("https://youtube.cl/")
    

@login_required
def tareas(request):
    tareas = Tarea.objects.all()
    categoria = CategoriaTarea.objects.all()
    return render(request, "tareas.html", {"tareas": tareas, "categorias": categoria})

def formTareas(request):
    categoria = CategoriaTarea.objects.all()
    return render(request, "crear_tarea.html", {"categorias": categoria})
