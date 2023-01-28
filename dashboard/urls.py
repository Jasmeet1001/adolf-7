from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_page, name='dashboard-admin'),
    path('distributer/', views.distributer_page, name='dashboard-distributer'),
    path('retailer/', views.retailer_page, name='dashboard-retailer'),
]