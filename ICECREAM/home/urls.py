from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.service, name='services'),
    path('contact/', views.contact, name='contact'),
    path('catageory/',views.catageory,name='catageory'),
    path('cart/',views.cart,name='cart'),
    path('search/', views.search_results, name='search_results'),  # Add this line for search functionality
]
