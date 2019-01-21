from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='minerals_home'),
    path('detail/<int:pk>/', views.mineral_detail, name='mineral_detail'),
    path('detail/random/', views.random_mineral, name='random_mineral'),
    path('letter/<letter>/', views.alphabet, name='alphabet_mineral'),
    path('search/', views.search_mineral, name='search_mineral'),
    path('group/<group_name>/', views.group_mineral, name='group_mineral'),

]

