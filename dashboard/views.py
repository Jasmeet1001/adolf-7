from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

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
                        # Distributer.objects.create()
                        temp = admin_form.save(commit=False)
                        temp.user = user
                        temp.save()

                        messages.success(request, 'New Admin Added')

                if option == '2':
                    dist_form = NewDist(request.POST, instance=request.user)
                    # user_form = UserCreationForm(request.POST)
                    if dist_form.is_valid() and user_form.is_valid():
                        # pnum = user_form.cleaned_data.get('phone_number')
                        # fnm = user_form.cleaned_data.get('first_name')
                        # lnm = user_form.cleaned_data.get('last_name')
                        # email = user_form.cleaned_data.get('email')
                        # pwd = user_form.cleaned_data.get('password')
                        # user = User.objects.create_user(phone_number=pnum, password=pwd, first_name=fnm, last_name=lnm, email=email)
                        # Distributer.objects.create()
                        temp = dist_form.save(commit=False)
                        temp.user = user
                        temp.save()
                        messages.success(request, 'New Distributer Added')

                elif option == '3':
                    ret_form = NewRet(request.POST)
                    # user_form = UserCreationForm(request.POST)
                    if ret_form.is_valid() and user_form.is_valid():
                        # pnum = user_form.cleaned_data.get('phone_number')
                        # fnm = user_form.cleaned_data.get('first_name')
                        # lnm = user_form.cleaned_data.get('last_name')
                        # email = user_form.cleaned_data.get('email')
                        # pwd = user_form.cleaned_data.get('password')
                        # user = User.objects.create_user(phone_number=pnum, password=pwd, first_name=fnm, last_name=lnm, email=email)
                        # Distributer.objects.create()
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

@login_required
@user_passes_test(is_admin)
def admin_page(request):
    distributers_all = request.user.adolfadmin.distributers.all()

    context = {
        'dist_obj': distributers_all
    }

    return render(request, 'dashboard/admin.html', context)

@login_required
def order_view(request):
    pricelist_all = PriceList.objects.filter(id__lt=190)
    # pricelist_all = PriceList.objects.all()

    context = {
        'pricelist_obj': pricelist_all
    }

    return render(request, 'dashboard/neworder.html', context)

@login_required
@user_passes_test(is_distributer)
def distributer_page(request):
    return render(request, 'dashboard/distributer.html')

@login_required
@user_passes_test(is_retailer)
def retailer_page(request):
    return render(request, 'dashboard/retailer.html')