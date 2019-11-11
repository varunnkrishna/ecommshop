from django.urls import path, include
from . import views

urlpatterns = [
    path('addcart/', views.cartapp, name='cartapp'),
    path('insertcart/', views.insertcart, name='insertcart'),
    path('viewcart/', views.viewcart, name='viewcart'),
    path('delete/', views.delete, name='delete'),
    path('modifycart/', views.modifycart, name='modifycart'),
    path('modifiedcart',views.modifiedcart),


 
]
