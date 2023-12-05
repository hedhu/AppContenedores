from django.urls import path
from contenedores import views
from .views import *

urlpatterns = [
    path('inicio/', views.index, name='inicio'),
    path('buscador/', ContenedoresListView.as_view(), name='buscador'),
    path('contenedor/<str:contenedor_codigo>/', ContenedorDetailView.as_view(), name='contenedor'),
    path('administrador/usuario_lista/', UsuarioListView.as_view(), name='usuario_lista'),
    path('administrador/usuario_crear/', UsuarioCreateView.as_view(), name='usuario_crear'),
    path('administrador/usuario_eliminar/<int:pk>/', UsuarioDeleteView.as_view(), name='usuario_eliminar'),
    path('temporal/', views.temporal, name='temporal'),
    path('list_contenedores/', views.list_contenedores, name='list_contenedores'),
] 
