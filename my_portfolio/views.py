from django.shortcuts import render
from .models import Project

#Configuracion de vistas
def home(request):
    projects = Project.objects.all() #Trae todos los proyectos guardados que tenemos en Project a traves de Object.all 
    return render(request, 'home.html', {'myprojects': projects})