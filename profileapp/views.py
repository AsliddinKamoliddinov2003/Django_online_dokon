from django.db import connection
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


def account_view(request):
    return render(request, 'profile/account.html')


@login_required(login_url="/account/login/")
def settings_view(request):
    client = ClientProfile.objects.get(account=request.user)
    user = request.user
    if not client:
        form = ClientForm()
        if request.method == "POST":
            form = ClientForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                form_data = form.cleaned_data
                try:
                    user.first_name=form_data['first_name']
                    user.last_name=form_data['last_name']
                    user.email=form_data['email']
                    user.save()
                except:
                    pass
    else:
        form = ClientForm(instance=client)
        if request.method == "POST":
            form = ClientForm(request.POST, request.FILES, instance=client)
            if form.is_valid():
                form.save()
                form_data = form.cleaned_data
                try:
                    user.first_name=form_data['first_name']
                    user.last_name=form_data['last_name']
                    user.email=form_data['email']
                    user.save()
                except:
                    pass

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
 

