from django.shortcuts import render



def account_view(request):
    return render(request, 'profile/account.html')

def settings_view(request):
    return render(request, 'profile/settings.html')

def selling_view(request):
    return render(request, 'profile/sellings.html')

def order_view(request):
    return render(request, 'profile/orders.html')

def adress_view(request):
    return render(request, 'profile/address.html')
 

