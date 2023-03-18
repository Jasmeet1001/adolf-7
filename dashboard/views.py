from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator

from .models import PriceList, AdolfAdmin, Distributer, Retailer

# Create your views here.

def is_admin(user):
    return AdolfAdmin.objects.filter(user=user).exists()

def is_distributer(user):
    return Distributer.objects.filter(user=user).exists()

def is_retailer(user):
    return Retailer.objects.filter(user=user).exists()

@login_required
@user_passes_test(is_admin)
def admin_page(request):
    distributers_all = request.user.adolfadmin.distributers.all()

    context = {
        'dist_obj': distributers_all
    }

    return render(request, 'dashboard/admin.html', context)

@login_required
def pricelist_view(request):
    pricelist_all = PriceList.objects.all()

    context = {
        'pricelist_obj': pricelist_all
    }

    return render(request, 'dashboard/pricelist.html', context)

@login_required
@user_passes_test(is_distributer)
def distributer_page(request):
    return render(request, 'dashboard/distributer.html')

@login_required
@user_passes_test(is_retailer)
def retailer_page(request):
    return render(request, 'dashboard/retailer.html')