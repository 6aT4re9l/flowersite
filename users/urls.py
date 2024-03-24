﻿from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path("login/", views.register_or_login, name="register_or_login"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile, name="profile"),
]
