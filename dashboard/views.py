from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.contrib import messages

from .forms import UserRole, NewDist, NewRet, NewAdmin, UserCreation
from .models import PriceList, AdolfAdmin, Distributer, Retailer
from register.models import User

# Create your views here.

def is_admin(user):
    return AdolfAdmin.objects.filter(user=user).exists()

def is_distributer(user):
    return Distributer.objects.filter(user=user).exists()

def is_retailer(user):
    return Retailer.objects.filter(user=user).exists()

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

                if option == '2':
                    dist_form = NewDist(request.POST, instance=request.user)
                    if dist_form.is_valid() and user_form.is_valid():
                        temp = dist_form.save(commit=False)
                        temp.user = user
                        temp.save()
                        messages.success(request, 'New Distributer Added')

                elif option == '3':
                    ret_form = NewRet(request.POST)
                    if ret_form.is_valid() and user_form.is_valid():
                        temp = ret_form.save(commit=False)
                        temp.user = user
                        temp.save()
                        messages.success(request, 'New Retailer Added')
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

    # all_retailers = [i for i in retailers_all(distributers_all)]

    context = {
        'dist_obj': distributers_all,
        # 'ret_obj': all_retailers[0],
        'ret_obj': retailers_all(distributers_all),
    }

    return render(request, 'dashboard/admin.html', context)

@login_required
def order_view_admin(request):
    # pricelist_all = PriceList.objects.filter(id__lt=190)
    pricelist_all = PriceList.objects.all()
    
    context = {
        'pricelist_obj': pricelist_all,
    }

    return render(request, 'dashboard/neworderAdmin.html', context)


@login_required
def order_view_distributor(request):
    pricelist_all = PriceList.objects.filter(id__lt=190)
    # pricelist_all = PriceList.objects.all()

    context = {    
        'pricelist_obj': pricelist_all,
    }


    return render(request, 'dashboard/neworderDistributor.html', context)

@login_required
def order_view_retailer(request):
    pricelist_all = PriceList.objects.filter(id__lt=190)
    # pricelist_all = PriceList.objects.all()

    context = {    
        'pricelist_obj': pricelist_all,
    }


    return render(request, 'dashboard/neworderRetailer.html', context)

@login_required
@user_passes_test(is_distributer)
def distributor_page(request):
    return render(request, 'dashboard/distributer.html')

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