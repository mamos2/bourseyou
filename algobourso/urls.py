from django.urls import path
from django.contrib import admin
from algobourso import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accueil/', views.index),
]