from django.shortcuts import render, redirect
from .forms import ToDoListForm
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
	tasks = [task for task in ToDoList.objects.all()]

	return render(request, "todo_app/home.html", {"tasks" : tasks})


def new_task(request):
	form = ToDoListForm()
	if request.method == "POST":
		form = ToDoListForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home_page')

	return render(request, "todo_app/new_task.html", {"form" : form})


def task_update(request):
	return render(request, "todo_app/task_update.html")


def task_view(request):
	tasks = [task for task in ToDoList.objects.all()]

	return render(request, "todo_app/task_view.html", {"tasks" : tasks})