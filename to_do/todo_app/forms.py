from django.forms import ModelForm
from .models import ToDoList


class ToDoListForm(ModelForm):
	class Meta:
		model = ToDoList
		fields = '__all__'