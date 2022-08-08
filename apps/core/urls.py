from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('reservation', views.reservation, name='reservation'),
    path('reservation/<pk>', views.reservation_pk, name='reservation_pk'),
    path('workstations', views.workstations, name='workstations'),
    path('workstations/<pk>', views.workstations_pk, name='workstations_pk'),
]
