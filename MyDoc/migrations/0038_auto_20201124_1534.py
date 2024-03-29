# Generated by Django 3.1.3 on 2020-11-24 12:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MyDoc', '0037_auto_20201124_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medrecs',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 24, 12, 34, 7, 953120, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='userappointment',
            name='consultation_type',
            field=models.CharField(choices=[('', ''), ('Online Consultation', 'Online Consultation'), ('Face-Face Consultation', 'Face-Face Consultation')], default='', max_length=30, null=True),
        ),
        migrations.DeleteModel(
            name='Consultation',
        ),
    ]
