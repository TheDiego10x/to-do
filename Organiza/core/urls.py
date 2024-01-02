from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tareas", views.tareas, name="tareas"),
    path("crear_tarea", views.formTareas, name="formTareas"),
    path("logout", views.logout_view, name="logout_view")
]