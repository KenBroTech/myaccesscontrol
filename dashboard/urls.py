from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='dashboard-index'),
    path('caesar/', views.caesar, name='dashboard-caesar'),
    path('aes/', views.aes, name='dashboard-aes'),
    path('caution/', views.caution, name='dashboard-caution'),
]
