# Generated by Django 2.2.1 on 2019-06-18 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0004_auto_20190618_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('contactno', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('complaint_type', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]
