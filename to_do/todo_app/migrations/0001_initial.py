# Generated by Django 3.1.5 on 2021-02-16 21:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=60, unique=True)),
                ('description', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]