from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def admin_page(request):
    return render(request, 'dashboard/admin.html')

@login_required
def distributer_page(request):
    return render(request, 'dashboard/distributer.html')

@login_required
def retailer_page(request):
    return render(request, 'dashboard/retailer.html')