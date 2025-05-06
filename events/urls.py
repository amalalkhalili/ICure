from lib2to3.pytree import generate_matches

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logged_in/', views.logged_in, name='logged_in'),
    path('logout/',views.logout_user,name='logout'),
    path('diagnose/', views.diagnose, name='diagnose'),
    path('find_doctor/', views.find_doctor, name='find_doctor'),
    path('find_specs/', views.find_specs, name='find_specs'),
    path('doctor_result/', views.doctor_result, name='doctor_result'),
    path('profile/', views.profile, name='profile'),
    path('medical_history/', views.medical_history, name='medical_history'),
    path('find_hospitals/', views.find_hospitals, name='find_hospitals'),
    path('hospitals_result/', views.hospital_result, name='hospital_result'),
    path('hospitals/', views.hospitals, name='hospitals'),
    path('search_symptoms/', views.select_symptoms, name='search_symptoms'),
    path('result/', views.result, name='result'),
]
