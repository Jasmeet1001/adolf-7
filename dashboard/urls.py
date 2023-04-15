from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_page, name='dashboard-admin'),
    path('admin/create-user/', views.create_new_user, name='admin-createuser'),
    path('admin/pricelist/', views.order_view_admin, name='order-view-admin'),
    path('distributor/', views.distributor_page, name='dashboard-distributor'),
    path('distributor/pricelist/', views.order_view_distributor, name='order-view-distributor'),
    path('retailer/', views.retailer_page, name='dashboard-retailer'),
    path('retailer/pricelist', views.order_view_retailer, name='order-view-retailer'),
]