from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_page, name='dashboard-admin'),
    path('admin/create-user', views.create_new_user, name='admin-createuser'),
    path('admin/pricelist/', views.pricelist_view, name='pricelist-view'),
    path('distributer/', views.distributer_page, name='dashboard-distributer'),
    path('retailer/', views.retailer_page, name='dashboard-retailer'),
]