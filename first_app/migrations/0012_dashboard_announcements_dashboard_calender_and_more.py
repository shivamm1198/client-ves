# Generated by Django 4.2.6 on 2023-11-01 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0011_rename_userlogin_dashboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='announcements',
            field=models.TextField(default='Unknown Address', max_length=100),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='calender',
            field=models.TextField(default='Unknown Address', max_length=100),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='feedback',
            field=models.TextField(default='Unknown Address', max_length=100),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='profile',
            field=models.TextField(default='Unknown Address', max_length=100),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='tasks',
            field=models.TextField(default='Unknown Address', max_length=100),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='team_members',
            field=models.TextField(default='Unknown Address', max_length=100),
        ),
    ]
