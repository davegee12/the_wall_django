from django.shortcuts import render, HttpResponse, redirect
from .models import Users
from django.contrib import messages
from datetime import datetime


def index(request):
    return render(request, 'log_and_reg_app/index.html')

def success(request):
    if 'user_id' not in request.session:
        messages.error(request, "Please login!")
        return redirect("/")
    else:
        context = {
            "user": Users.objects.get(id = request.session['user_id'])
        }
    return render(request, 'log_and_reg_app/success.html', context)

def create_user(request):
    if request.method == "POST":
        errors = Users.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else:
            new_user = Users.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], birthday = request.POST['birthday'], email = request.POST['email'], password = request.POST['password'])
            messages.success(request, "User successfully added!")
            request.session['user_id'] = new_user.id
        return redirect("/wall")

def login(request):
    if request.method == "POST":
        errors = Users.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else:
            returning_user = Users.objects.get(email = request.POST['email'])
            messages.success(request, "User successfully logged in!")
            request.session['user_id'] = returning_user.id
            return redirect("/wall")

def log_out(request):
    request.session.clear()
    return redirect("/")