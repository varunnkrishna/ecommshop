from django.urls import path, include
from . import views

urlpatterns = [
    path('addcart/', views.cartapp, name='cartapp'),
 
]