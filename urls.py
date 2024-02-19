"""
URL configuration for torremolinosSports project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio),

    path('deportes/', views.DeportesListView.as_view(), name='deportes_lista'),
    path('deportes/create', views.DeporteCreateView.as_view(), name='deportes_create'),
    path('deportes/<int:pk>/update/', views.DeportesListView.as_view(), name='deportes_update'),
    path('deportes/<int:pk>/delete/', views.DeportesListView.as_view(), name='deportes_delete'),

    path('instalaciones/', views.InstalacionesListView.as_view(), name='instalaciones_lista'),
    path('instalaciones/create', views.InstalacionCreateView.as_view(), name='instalaciones_create'),
    path('instalaciones/<int:pk>/update/', views.InstalacionUpdateView.as_view(), name='instalaciones_update'),
    path('instalaciones/<int:pk>/delete/', views.InstalacionDeleteView.as_view(), name='instalaciones_delete'),

    path('equipos/', views.EquiposListView.as_view(), name='equipos_lista'),
    path('equipos/create/', views.EquipoCreateView.as_view(), name='equipo_create'),
    path('equipos/<int:pk>/', views.EquipoDetailView.as_view(), name='equipo_detalle'),
    path('equipos/<int:pk>/update/', views.EquipoUpdateView.as_view(), name='equipo_update'),
    path('equipos/<int:pk>/delete/', views.EquipoDeleteView.as_view(), name='equipo_delete'),
    path('equipos/<int:pk>/jugadores/nuevo/', views.JugadorCreateView.as_view(), name='jugador_create'),

]
