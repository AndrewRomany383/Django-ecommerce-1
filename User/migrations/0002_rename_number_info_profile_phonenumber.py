# Generated by Django 4.0.5 on 2022-10-28 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='number_info',
            new_name='phonenumber',
        ),
    ]
