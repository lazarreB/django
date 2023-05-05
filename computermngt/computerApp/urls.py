from django.urls import path
from . import views

urlpatterns = [
    path ('',views.index, name='index'),
    path ('machine/', views.machine_list_view, name = 'machines'),
    path ('personne/', views.personne_list_view, name = 'personnes'),
]