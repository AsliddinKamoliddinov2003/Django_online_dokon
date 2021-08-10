from django.urls import path

from .views import *


urlpatterns = [
    path("", index, name="news-list"),
    path("create/", create , name="news-careate"),
    path("update/<int:pk>/", update, name="news-update"),
    path("delete/<int:pk>/", delete, name="news-delete"),

]