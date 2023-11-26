from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from contenedores import views
import registration.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.buscador, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include(registration.urls)),
    path('buscador/', views.buscador, name='buscador'),
    path('contenedor/', views.contenedor, name='contenedor'),
]

