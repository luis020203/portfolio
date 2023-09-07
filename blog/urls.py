from django.urls import path

from .views import render_post, render_publics     #Importacion de vistas


app_name = 'blogs'

urlpatterns = [
    path('', render_post, name="posts"),
    path('<int:post_id>', render_publics, name="publics"), #Desde Views me retorna el Post consultado
]
