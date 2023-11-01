from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from contenedores import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.buscador, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('buscador/', views.buscador, name='buscador'),
]
