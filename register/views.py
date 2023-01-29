from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def login_check(request):
    if request.method == "POST":
        phone_num = request.POST.get('phone_number')
        password = request.POST.get('password')

        user = authenticate(phone_number=phone_num, password=password)
        if user:
            if user.is_active:  # type: ignore 
                login(request, user)
                if user.is_adolf_staff:  # type: ignore 
                    return redirect('dashboard-admin')
                elif user.is_distributer:  # type: ignore 
                    return redirect('dashboard-distributer')
                elif user.is_retailer:  # type: ignore 
                    return redirect('dashboard-retailer')
            else:
                messages.error(request, "This account is inactive.")
        else:
            messages.error(request, "You have entered an invalid email / password combination.")

        return redirect('login-view')
    return render(request, 'register/login.html')