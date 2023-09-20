# Generated by Django 4.2.5 on 2023-09-20 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('phoneno', models.CharField(max_length=10)),
                ('join_date', models.DateField()),
                ('region', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]