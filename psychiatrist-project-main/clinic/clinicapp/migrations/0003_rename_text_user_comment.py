# Generated by Django 4.2.5 on 2024-06-10 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinicapp', '0002_user_surname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='text',
            new_name='comment',
        ),
    ]
