from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


def home_view(request):
    return render(request, "accounts/home.html")


def user_login(request):
    error = ""
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_url = request.GET.get("next", "profile")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(next_url)
        else:
            error = "Invalid username or password"

    return render(request, "accounts/login.html", {"error": error})


@login_required
def profile_view(request):
    return render(request, "accounts/profile.html")

@csrf_exempt
@login_required
def change_email_vulnerable(request):
    new_email = request.GET.get("email")

    if new_email:
        request.user.email = new_email
        request.user.save()
        return redirect("profile")

    return render(request, "accounts/change_email_vulnerable.html")

@login_required
def change_email_safe(request):
    if request.method == "POST":
        new_email = request.POST.get("email")
        request.user.email = new_email
        request.user.save()
        return redirect("profile")
 
    return render(request, "accounts/change_email_safe.html")