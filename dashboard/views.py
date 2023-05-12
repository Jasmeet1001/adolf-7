from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.contrib import messages
from django.views.generic import UpdateView
from django.db.models import Q

from .forms import UserRole, NewDist, NewRet, NewAdmin, UserCreation
from .models import PriceList, AdolfAdmin, Distributer, Retailer
from register.models import User

import random

# Create your views here.

def is_admin(user):
    return AdolfAdmin.objects.filter(user=user).exists()

def is_distributer(user):
    return Distributer.objects.filter(user=user).exists()

def is_retailer(user):
    return Retailer.objects.filter(user=user).exists()

class AdminUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = AdolfAdmin
    fields = '__all__'
    template_name = 'dashboard/admin_update_view.html'

    def test_func(self):
        return is_admin(self.request.user)

class PriceListUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PriceList
    fields = '__all__'
    template_name = 'dashboard/pricelist_edit.html'

    def test_func(self):
        return is_admin(self.request.user)

class DistributorUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = Distributer
    fields = '__all__'
    template_name = 'dashboard/distributor_update_view.html'

    def test_func(self):
        return is_distributer(self.request.user)

class RetailerUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = Retailer
    fields = '__all__'
    template_name = 'dashboard/retailer_update_view.html'

    def test_func(self):
        return is_retailer(self.request.user)


@login_required
@user_passes_test(is_admin)
def create_new_user(request):
    admin_form = NewAdmin()
    dist_form = NewDist()
    ret_form = NewRet()
    user_form = UserCreation()

    if request.method == 'POST':
        userrole_form = UserRole(request.POST)
        if userrole_form.is_valid():
            option = userrole_form.cleaned_data.get('choices')
            user_form = UserCreation(request.POST)
            if user_form.is_valid():
                pnum = user_form.cleaned_data.get('phone_number')
                fnm = user_form.cleaned_data.get('first_name')
                lnm = user_form.cleaned_data.get('last_name')
                email = user_form.cleaned_data.get('email')
                pwd = user_form.cleaned_data.get('password')
                user = User.objects.create_user(phone_number=pnum, password=pwd, first_name=fnm, last_name=lnm, email=email)

                if option == '1':
                    admin_form = NewAdmin(request.POST)
                    if admin_form.is_valid() and user_form.is_valid():
                        temp = admin_form.save(commit=False)
                        temp.user = user
                        temp.save()
                        messages.success(request, 'New Admin Added')
                        return redirect('admin-createuser')

                if option == '2':
                    dist_form = NewDist(request.POST)
                    if dist_form.is_valid() and user_form.is_valid():
                        temp = dist_form.save(commit=False)
                        temp.user = user
                        temp.save()
                        messages.success(request, 'New Distributer Added')
                        return redirect('admin-createuser')


                elif option == '3':
                    ret_form = NewRet(request.POST)
                    if ret_form.is_valid() and user_form.is_valid():
                        temp = ret_form.save(commit=False)
                        temp.user = user
                        temp.save()
                        messages.success(request, 'New Retailer Added')
                        return redirect('admin-createuser')
    else:
        userrole_form = UserRole()
    
    context = {
        'role_form': userrole_form,
        'user_form': user_form,
        'admin_form': admin_form,
        'dist_form': dist_form,
        'ret_form': ret_form
    }

    return render(request, 'dashboard/newuser.html', context)

def retailers_all(dist):
    for distributer in dist:
        yield distributer.retailers.all()

@login_required
@user_passes_test(is_admin)
def admin_page(request):
    distributers_all = request.user.adolfadmin.distributers.all()

    all_retailers = [i for i in retailers_all(distributers_all)]

    if(len(all_retailers[0]) == 0):
        context = {
            'dist_obj': distributers_all,
            'ret_obj': '',
            'top_selling': PriceList.objects.last(),
            'random_value' : random.choice([i for i in range(100)]) 
        }
    else:
        context = {
            'dist_obj': distributers_all,
            'ret_obj': all_retailers[0],
            'top_selling': PriceList.objects.last(),
            'random_value' : random.choice([i for i in range(100)])     
        }  

    return render(request, 'dashboard/admin.html', context)

@login_required
def order_view_admin(request):
    search_res = ''
    q_query = Q()
    pricelist_all = PriceList.objects.all()
    if request.GET.get('search-query'):
        search_res = request.GET.get('search-query')
        if not(any([request.GET.get('UOM') or request.GET.get('Color') or request.GET.get('Product Name') or request.GET.get('Vehicle Type')])):
            print('elif')
            pricelist_all = pricelist_all.filter(Q(vehical_type__icontains=search_res)|Q(product_name__icontains=search_res)|Q(color__icontains=search_res)|Q(uom__icontains=search_res)).order_by('-id')
        else:
            if request.GET.get('Vehicle Type'):
                q_query |= Q(vehical_type__icontains=search_res)
            if request.GET.get('Product Name'):
                q_query |= Q(product_name__icontains=search_res)
            if request.GET.get('Color'):
                q_query |= Q(color__icontains=search_res)
            if request.GET.get('UOM'):
                q_query |= Q(uom__icontains=search_res)
            
            pricelist_all = pricelist_all.filter(q_query)
        
    paginator = Paginator(pricelist_all, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'pricelist_obj': page_obj,
    }

    return render(request, 'dashboard/neworderAdmin.html', context)


@login_required
def order_view_distributor(request):
    search_res = ''
    q_query = Q()
    pricelist_all = PriceList.objects.all()
    if request.GET.get('search-query'):
        search_res = request.GET.get('search-query')
        if not(any([request.GET.get('UOM') or request.GET.get('Color') or request.GET.get('Product Name') or request.GET.get('Vehicle Type')])):
            print('elif')
            pricelist_all = pricelist_all.filter(Q(vehical_type__icontains=search_res)|Q(product_name__icontains=search_res)|Q(color__icontains=search_res)|Q(uom__icontains=search_res)).order_by('-id')
        else:
            if request.GET.get('Vehicle Type'):
                q_query |= Q(vehical_type__icontains=search_res)
            if request.GET.get('Product Name'):
                q_query |= Q(product_name__icontains=search_res)
            if request.GET.get('Color'):
                q_query |= Q(color__icontains=search_res)
            if request.GET.get('UOM'):
                q_query |= Q(uom__icontains=search_res)
            
            pricelist_all = pricelist_all.filter(q_query)
        
    paginator = Paginator(pricelist_all, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'pricelist_obj': page_obj,
    }

    return render(request, 'dashboard/neworderDistributor.html', context)

@login_required
def order_view_retailer(request):
    search_res = ''
    q_query = Q()
    pricelist_all = PriceList.objects.all()
    if request.GET.get('search-query'):
        search_res = request.GET.get('search-query')
        if not(any([request.GET.get('UOM') or request.GET.get('Color') or request.GET.get('Product Name') or request.GET.get('Vehicle Type')])):
            print('elif')
            pricelist_all = pricelist_all.filter(Q(vehical_type__icontains=search_res)|Q(product_name__icontains=search_res)|Q(color__icontains=search_res)|Q(uom__icontains=search_res)).order_by('-id')
        else:
            if request.GET.get('Vehicle Type'):
                q_query |= Q(vehical_type__icontains=search_res)
            if request.GET.get('Product Name'):
                q_query |= Q(product_name__icontains=search_res)
            if request.GET.get('Color'):
                q_query |= Q(color__icontains=search_res)
            if request.GET.get('UOM'):
                q_query |= Q(uom__icontains=search_res)
            
            pricelist_all = pricelist_all.filter(q_query)
        
    paginator = Paginator(pricelist_all, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'pricelist_obj': page_obj,
    }

    return render(request, 'dashboard/neworderRetailer.html', context)

def add_to_cart(request):
    if request.GET.get(''):
        pass

@login_required
@user_passes_test(is_distributer)
def distributor_page(request):
    retailer_all = request.user.distributer.retailers.all()

    context = {
        'ret_obj': retailer_all,
    }  

    return render(request, 'dashboard/distributer.html', context)

@login_required
@user_passes_test(is_retailer)
def retailer_page(request):
    return render(request, 'dashboard/retailer.html')


@login_required
def order_sucessful_distributor(request):
    return render(request, 'dashboard/orderConfirmedDistributor.html')


@login_required
def order_sucessful_retailer(request):
    return render(request, 'dashboard/orderConfirmedRetailer.html')