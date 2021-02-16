from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.data.get('username')
            password = form.data.get("password1")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('/users/login')

    return render(request, "users/register.html", {'form': form})


def user_logout(request):
	logout(request)
	return redirect("home_page")