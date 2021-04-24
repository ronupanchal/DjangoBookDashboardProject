# Generated by Django 3.1.1 on 2020-10-01 19:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(default=datetime.datetime(2020, 10, 2, 0, 51, 40, 135343))),
                ('end', models.DateTimeField(default=datetime.datetime(2020, 10, 2, 0, 51, 40, 135343))),
                ('eventname', models.CharField(help_text='Enter a event name (e.g. Workshop, Seminar etc.)', max_length=200)),
                ('uid', models.IntegerField(max_length=5)),
            ],
        ),
    ]
