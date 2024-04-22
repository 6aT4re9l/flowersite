from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
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
                messages.success(request, username, "Вы успешно вышли в аккаунт")
                redirect_page = request.POST.get("next", None)
                if redirect_page and redirect_page != reverse("user:logout"):
                    return HttpResponseRedirect(request.POST.get("next"))

                return HttpResponseRedirect(reverse("main:index"))
        elif registr_form.is_valid():
            registr_form.save()
            user = registr_form.save()
            auth.login(request, user)
            messages.success(request, user.username, "Вы успешно вышли в аккаунт")
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


def users_cart(request):
    return render(request, "users/users_cart.html")


@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse("main:index"))
