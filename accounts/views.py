from accounts.forms import UserRegisterForm, UserLoginForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import User



def register_account(request):
    form = UserRegisterForm()

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        "form":form
    }
    return render(request, "account/register.html", context)


def login_account(request):
    form = UserLoginForm()

    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = authenticate(request, email=email, password=password)

            if user:
                login(request, user=user)
                next_page = request.GET.get("next", None)
                if next_page:
                    return redirect(next_page)
                else:
                    return redirect(reverse("store-page"))
           
    context = {
        "form": form
    }
    return render(request, "account/login.html", context)



def account_logout(request):
    if request.method == "POST":
        logout(request)

    return redirect(reverse("account-login"))