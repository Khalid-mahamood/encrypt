# Generated by Django 3.2.10 on 2022-12-15 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projapp', '0003_rename_name_encrypt_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='encrypt',
            old_name='subject',
            new_name='name',
        ),
    ]
