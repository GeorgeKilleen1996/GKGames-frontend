# Generated by Django 4.2.2 on 2023-07-01 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_module_perms',
            field=models.BooleanField(default=False),
        ),
    ]