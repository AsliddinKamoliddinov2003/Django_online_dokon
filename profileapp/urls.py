from django.conf.urls.i18n import urlpatterns
from django.urls import path

from .views import *



urlpatterns = [
    path("account/", account_view, name="account-view"),
    path("settings/", settings_view, name="settings-view"),
    path("selling/", selling_view, name="selling-view"),
    path("order/", order_view, name="order-view"),
    path("adress/", adress_view, name="adress-view"),
]