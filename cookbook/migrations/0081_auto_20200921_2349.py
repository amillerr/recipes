# Generated by Django 3.0.7 on 2020-09-21 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0080_auto_20200921_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreference',
            name='shopping_auto_sync',
            field=models.IntegerField(default=5),
        ),
    ]