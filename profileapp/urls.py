from django.conf.urls.i18n import urlpatterns
from django.urls import path

from .views import *



urlpatterns = [
    path("account/", account_view, name="account-view"),
    path("settings/", settings_view, name="settings-view"),
    path("selling/", selling_view, name="selling-view"),
    path("order/", order_view, name="order-view"),
    path("adress/", adress_view, name="adress-view"),
    path("add_adress/", add_adress_view, name="add-adress-view"),
    path("update_adress/<int:pk>/", update_adress_view, name="update-adress-view"),
    path("delete_adress/<int:pk>/", delete_adress_view, name="delete-adress-view"),
    path("adress_active/<int:pk>/<str:k>/", adress_active_view, name="adress-active-view")
]