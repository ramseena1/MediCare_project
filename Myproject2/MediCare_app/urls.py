from django.urls import path

from MediCare_app import views

urlpatterns = [
    path('',views.Home_page,name='Home_page'),
    path('login',views.Login_page,name='Login_page'),
    path('Patient_Register_page',views.Patient_Register_page,name='Patient_Register_page'),
    path('Doctor_registration_page',views.Doctor_registration_page,name='Doctor_registration_page'),



]