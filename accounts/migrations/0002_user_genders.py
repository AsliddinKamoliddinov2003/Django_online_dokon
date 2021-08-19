# Generated by Django 3.2.5 on 2021-08-19 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='genders',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female')], default='m', max_length=10),
        ),
    ]
