from accounts.forms import UserRegisterForm, UserLoginForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login

from .models import User




def register_account(request):
    form = UserRegisterForm()

    if request.method=="POST":
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
            gmail = form.cleaned_data["gmail"]
            password = form.cleaned_data["password"]

        user = authenticate(request, gmail=gmail, password=password)

        if user:
            login(request, user=user)
            next_page = request.GET.get("next", None)
            if next_page:
                return redirect(reverse(next_page))
            else:
                return redirect(reverse("store-page"))
        
           
    context = {
        "form":form
    }
    return render(request, "account/login.html", context)