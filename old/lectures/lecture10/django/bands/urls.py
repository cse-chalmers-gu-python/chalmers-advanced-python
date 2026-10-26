from django.urls import path
from . import views

urlpatterns = [
    path('bands/', views.home),
]
