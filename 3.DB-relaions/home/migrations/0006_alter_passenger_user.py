# Generated by Django 5.1 on 2024-08-29 10:07

import home.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_passenger_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='user',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=models.SET(home.models.set_delete_user), to=settings.AUTH_USER_MODEL),
        ),
    ]
