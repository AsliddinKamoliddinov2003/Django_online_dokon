# Generated by Django 3.2.5 on 2021-12-06 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0005_alter_address_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientprofile',
            name='pochta_code',
        ),
    ]