from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.register, name='register'),
    path('login/',views.login),
    path('my_logout',views.my_logout),
    path('signup/otpvalidation',views.otpvalidation),

]
