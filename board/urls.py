from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('<int:pk>/', views.inquiry_detail, name='inquiry_detail'),
    path('create/', views.inquiry_create, name='inquiry_create'),
    path('', views.main_page, name='main_page'),
]