# Generated by Django 3.1 on 2020-08-18 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Language',
            new_name='Genre',
        ),
    ]