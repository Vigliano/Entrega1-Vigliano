from django.urls import path 
from Miapp import views

urlpatterns = [
    path('', views.index_html),
    path('auto_html', views.auto_html, name='Auto'),
    path('camioneta_html', views.camioneta_html, name='Camioneta'),
    path('moto_html', views.moto_html, name='Moto'),
    path('insertar_auto', views.insertar_auto, name='Insertar Auto'),
    path('insertar_moto', views.insertar_moto, name='Insertar Moto'),
    path('insertar_camioneta', views.insertar_camioneta, name='Insertar Camioneta'),
    path('buscar_auto', views.buscar_auto, name='Buscar Auto'),
    path('buscar_camioneta', views.buscar_camioneta, name='Buscar Camioneta'),
    path('buscar_moto', views.buscar_moto, name='Buscar Moto'),
    
    


]
