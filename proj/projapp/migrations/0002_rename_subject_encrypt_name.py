# Generated by Django 3.2.10 on 2022-12-15 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='encrypt',
            old_name='subject',
            new_name='name',
        ),
    ]
