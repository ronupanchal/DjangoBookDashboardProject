# Generated by Django 3.1 on 2020-08-21 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0005_book'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name']},
        ),
    ]
