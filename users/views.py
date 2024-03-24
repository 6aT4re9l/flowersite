from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from users.forms import UserLoginForm, UserRegistrationForm
from django.urls import reverse


def register_or_login(request):
    if request.method == "POST":
        registr_form = UserRegistrationForm(data=request.POST)
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            log_user = auth.authenticate(username=username, password=password)
            if log_user:
                auth.login(request, log_user)
                return HttpResponseRedirect(reverse("main:index"))
        elif registr_form.is_valid():
            registr_form.save()
            user = registr_form
            auth.login(request, user)
            return HttpResponseRedirect(reverse("main:index"))
    else:
        registr_form = UserRegistrationForm()
        login_form = UserLoginForm()
    return render(
        request,
        "users/login.html",
        {
            "registr_form": registr_form,
            "login_form": login_form,
            "title": "Регистрация",
        },
    )


def profile(request):
    context = {
        "title": "Личный кабинет",
    }
    return render(request, "", context)


def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse("main:index"))
