# Generated by Django 3.2.20 on 2023-07-24 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_team2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team2',
            old_name='desc',
            new_name='desc2',
        ),
        migrations.RenameField(
            model_name='team2',
            old_name='img',
            new_name='img2',
        ),
        migrations.RenameField(
            model_name='team2',
            old_name='name',
            new_name='name2',
        ),
    ]
