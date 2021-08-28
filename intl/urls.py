from django.urls import path

from . import views


urlpatterns = [
    path("intl/", views.intl, name="intl")
]