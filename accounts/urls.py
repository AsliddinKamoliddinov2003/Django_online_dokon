from django.urls import path


from .views import login_account, register_account


urlpatterns = [
    path("register/", register_account, name="account-register" ),
    path("login/", login_account, name="account-login" )
]