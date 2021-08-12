from django.urls import path

from .views import *


urlpatterns = [
    path("", index, name="news-list"),
    path("create/", create , name="news-careate"),
    path("update/<int:pk>/", update, name="news-update"),
    path("delete/<int:pk>/", delete, name="news-delete"),
    path("home/", home, name="home"),
    path("create_director/", create_director, name="create-director"),
    path("update_director/<int:pk>/", update_director, name="update-director"),
    path("delete_director/<int:pk>/", delete_director, name="delete-director"),

]