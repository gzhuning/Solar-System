from django.urls import path

from . import views

app_name = 'solar_system'

urlpatterns = [
    path('', views.home, name='home'),
    path('science/', views.science, name='science'),
    path('playground/', views.playground, name='playground'),
]
