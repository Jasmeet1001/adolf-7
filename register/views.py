from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from dashboard.models import AdolfAdmin, Retailer, Distributer

# Create your views here.
def login_check(request):
    if request.method == "POST":
        phone_num = request.POST.get('phone_number')
        password = request.POST.get('password')

        user = authenticate(phone_number=phone_num, password=password)
        if user:
            if user.is_active:  # type: ignore 
                login(request, user)
                if AdolfAdmin.objects.filter(user=user).exists():
                    return redirect('dashboard-admin')
                elif Distributer.objects.filter(user=user).exists():
                    return redirect('dashboard-distributor')
                elif Retailer.objects.filter(user=user).exists():
                    return redirect('dashboard-retailer')
            else:
                messages.error(request, "This account is inactive.")
        else:
            messages.error(request, "You have entered an invalid email / password combination.")

        return redirect('login-view')
    return render(request, 'register/login.html')