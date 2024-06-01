from django.urls import include, path
from django.shortcuts import render, redirect
from . import views

app_name = "Profile"

urlpatterns = [
    path("", views.get_profile, name="index"),
    path("profile/", views.get_profile, name="get_profile"),
    path("projects/", views.get_project, name="get_project"),
    path("projects/<str:project_name>", views.get_project, name="get_project"),
]