from django.urls import path
from api_vehiculos.views import vehiculo_api_view

urlpatterns=[
    path('crear-vehiculo',vehiculo_api_view.as_view()),
    path('actualizar-vehiculo/<int:pkid>',vehiculo_api_view.as_view(),name='actualizar'),
]