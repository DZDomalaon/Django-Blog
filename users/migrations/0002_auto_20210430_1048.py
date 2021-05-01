# Generated by Django 3.2 on 2021-04-30 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='firstname',
            field=models.CharField(blank=True, max_length=20, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='lastname',
            field=models.CharField(blank=True, max_length=20, verbose_name='last name'),
        ),
    ]