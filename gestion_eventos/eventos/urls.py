from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_eventos, name='listar_eventos'),  # Ruta vacía para listar eventos
    path('<int:evento_id>/', views.detalle_evento, name='detalle_evento'),    
    path('<int:evento_id>/registrar/', views.registrar_evento, name='registrar_evento'),  # Ruta para registrar usuarios
    path('<int:evento_id>/editar/', views.actualizar_evento, name='actualizar_evento'),
    path('registro/<int:registro_id>/editar/', views.actualizar_registro, name='actualizar_registro'),
    path('agregar/', views.agregar_evento, name='agregar_evento'),
    path('agregar_usuario/', views.agregar_usuario, name='agregar_usuario'),
    path('registrar/', views.registrar_evento, name='registrar_evento'),
    path('<int:evento_id>/eliminar/', views.eliminar_evento, name='eliminar_evento'),
    path('registro/<int:registro_id>/eliminar/', views.eliminar_registro, name='eliminar_registro'),


]
