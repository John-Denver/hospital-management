# Generated by Django 3.1.3 on 2020-11-19 21:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MyDoc', '0021_auto_20201119_1217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='To',
            new_name='to',
        ),
        migrations.AddField(
            model_name='medrecs',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 19, 21, 53, 22, 325096, tzinfo=utc), null=True),
        ),
    ]