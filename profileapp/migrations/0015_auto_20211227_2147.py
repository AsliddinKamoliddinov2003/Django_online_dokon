# Generated by Django 3.2.5 on 2021-12-27 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0014_clientprofile_pochta_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientprofile',
            name='pochta_code',
        ),
        migrations.AddField(
            model_name='address',
            name='pochta_code',
            field=models.CharField(max_length=25, null=True),
        ),
    ]