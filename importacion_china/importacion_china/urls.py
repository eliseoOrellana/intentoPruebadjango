"""
URL configuration for importacion_china project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from simulator import views 

#URL patterns se utilizan para asignar URL específicas a vistas o funciones en tu aplicación web

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.calcular_costo, name='calcular_costo'),
    path('calcular_costo/', views.calcular_costo, name='calcular_costo'),
    path('historial/', views.historial_consultas, name='historial_consultas'),
]

