# Generated by Django 2.2.5 on 2019-10-29 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('fname', models.CharField(max_length=20)),
                ('phno', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('uname', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('pwd', models.CharField(max_length=15)),
                ('cpwd', models.CharField(max_length=15)),
            ],
        ),
    ]
