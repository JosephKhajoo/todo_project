from django.db import models
from django.utils import timezone

# Create your models here.

class ToDoList(models.Model):
	task_name = models.CharField(max_length=60, unique=True)
	description = models.TextField()
	date = models.DateField(default=timezone.now)
	status = models.CharField(max_length=20)

	def __str__(self):
		return f"{self.task_name}"