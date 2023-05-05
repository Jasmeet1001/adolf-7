from django.urls import path
from . import views
from .views import AdminUpdateView, DistributorUpdateView, RetailerUpdateView, PriceListUpdateView

urlpatterns = [
    path('admin/', views.admin_page, name='dashboard-admin'),
    path('admin/<int:pk>/profile/', AdminUpdateView.as_view(), name='admin-update'),
    path('admin/create-user/', views.create_new_user, name='admin-createuser'),
    path('admin/pricelist/', views.order_view_admin, name='order-view-admin'),
    path('admin/pricelist/<int:pk>/edit/', PriceListUpdateView.as_view(), name='pricelist-edit'),

    path('distributor/', views.distributor_page, name='dashboard-distributor'),
    path('distributor/<int:pk>/profile/', DistributorUpdateView.as_view(), name='distributor-update'),
    path('distributor/pricelist/', views.order_view_distributor, name='order-view-distributor'),
    path('distributor/ordersucessful/', views.order_sucessful_distributor, name='order-sucessful-distributor'),
    
    path('retailer/', views.retailer_page, name='dashboard-retailer'),
    path('retailer/<int:pk>/profile/', RetailerUpdateView.as_view(), name='retailer-update'),
    path('retailer/pricelist/', views.order_view_retailer, name='order-view-retailer'),
    path('retailer/ordersucessful/', views.order_sucessful_retailer, name='order-sucessful-retailer'),
]