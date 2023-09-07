from django.shortcuts import render, get_object_or_404
from .models import Post

#Renderizacion de vista principal
def render_post(request):
    blog = Post.objects.all()#Recorremos los objetos que estan en el modelo, en este caso en Post
    return render(request, 'posts.html', {'post': blog})

#Renderizacion de vista Post
def render_publics(request, post_id):
    post = get_object_or_404(Post, pk=post_id)#Consulta de Post mediante el PK, en caso de que no exista mostrar Error 404
    return render(request, 'publics.html', {'post':post}) #Si existe la publicacion renderiza la vista para mostrar el Post consultado