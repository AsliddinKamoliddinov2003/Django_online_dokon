from django.urls import path


from .views import *


urlpatterns = [
    path("register/", register_account, name="account-register"),
    path("login/", login_account, name="account-login"),
    path("logout/", account_logout, name="account-logout"),
]