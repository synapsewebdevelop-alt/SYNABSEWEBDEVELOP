
from django.urls import path
from . import views

urlpatterns = [
    path('SYNAPSE/', views.create),
    path('DATA/',views.view),
    
]
