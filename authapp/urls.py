from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.register, name='register'),
    path('login/',views.login),
    path('my_logout',views.my_logout),
    path('signup/otpvalidation',views.otpvalidation),

]
