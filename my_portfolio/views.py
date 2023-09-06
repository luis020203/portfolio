from django.shortcuts import render
from .models import Project

#Configuracion de vistas
def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'myprojects': projects})