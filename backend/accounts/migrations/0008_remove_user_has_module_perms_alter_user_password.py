# Generated by Django 4.2.2 on 2023-07-01 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_user_has_module_perms_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='has_module_perms',
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
