from django.urls import path

from . import views

urlpatterns = [
    path('full_menu/', views.get_menu)
]
