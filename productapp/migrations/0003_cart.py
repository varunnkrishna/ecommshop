# Generated by Django 2.2.5 on 2019-11-05 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0002_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('pid', models.IntegerField()),
                ('units', models.IntegerField()),
                ('unitprice', models.DecimalField(decimal_places=4, max_digits=10)),
                ('tuprice', models.DecimalField(decimal_places=4, max_digits=10)),
            ],
        ),
    ]
