"""
URL configuration for setup project.

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
from app_unibet import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.apostas, name='apostas'),
    path('apostando/', views.registrar_aposta, name='registrar_aposta'),
    path('lista-apostas/', views.lista_apostas, name='lista_apostas'),
    path('carteira/', views.carteira, name='carteira'),
    path('depositar/', views.depositar, name='depositar'),
    path('sacar/', views.sacar, name='sacar'),
    path('checar-status/', views.checar_status, name='checar_status'),
]
