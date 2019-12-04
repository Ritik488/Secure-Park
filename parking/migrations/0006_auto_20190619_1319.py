# Generated by Django 2.2.1 on 2019-06-19 07:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0005_complaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='answer',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='registration',
            name='ques',
            field=models.CharField(choices=[('food', 'What is your favourite Food?'), ('place', 'Which is your favourite place to vacation'), ('city', 'What city you were born in?'), ('book', 'What is your favourite book?')], default='book', max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='dob',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='registration',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('male', 'Male'), ('others', 'Others')], default='male', max_length=10),
        ),
    ]