from django.urls import path

from . import views

urlpatterns = [
    path('full_menu/', views.get_menu),
    path('full_menu/<str:cuisine>/', views.menu_by_cuisine)
]
