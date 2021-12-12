from django.db import connection
from django.shortcuts import render

from .models import *
from .forms import *
from accounts.models import User


def account_view(request):
    return render(request, 'profile/account.html')


def settings_view(request):
    client = ClientProfile.objects.first()
    user = request.user
    if not client:
        print("1")
        form = ClientForm()
        if request.method == "POST":
            form = ClientForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                print("saqladi")    
    else:
        form = ClientForm(instance=client)
        print("2")
        if request.method == "POST":
            form = ClientForm(request.POST, request.FILES, instance=client)
            if form.is_valid():
                c = ClientProfile.objects.first()
                u = User.objects.first()
                form.save()
                print("saqladi2")

    context = {
        "form":form,
        "user":user,
        "client":client
    }

    return render(request, 'profile/settings.html', context)

def selling_view(request):
    return render(request, 'profile/sellings.html')

def order_view(request):
    return render(request, 'profile/orders.html')

def adress_view(request):
    return render(request, 'profile/address.html')
 

