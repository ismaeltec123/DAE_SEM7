from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.crear_evento, name='crear_evento'),
    path('listar/', views.listar_eventos, name='listar_eventos'),
    path('actualizar/<int:id>/', views.actualizar_evento, name='actualizar_evento'),
    path('eliminar/<int:id>/', views.eliminar_evento, name='eliminar_evento'),
    path('registrar/<int:evento_id>/', views.registrar_usuario, name='registrar_usuario'),
]


