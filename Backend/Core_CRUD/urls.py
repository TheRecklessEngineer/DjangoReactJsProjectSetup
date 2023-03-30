from django.urls import path
from Core_CRUD import views

urlpatterns = [
                path('', views.index), 
                path('login/', views.index)
                ]