from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='minerals_home'),
    path('detail/<int:pk>/', views.mineral_detail, name='mineral_detail'),

]
