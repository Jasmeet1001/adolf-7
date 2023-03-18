from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', views.admin_page, name='dashboard-admin'),
    path('admin/PriceList/', views.pricelist_view, name='pricelist-view'),
    path('distributer/', views.distributer_page, name='dashboard-distributer'),
    path('retailer/', views.retailer_page, name='dashboard-retailer'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)