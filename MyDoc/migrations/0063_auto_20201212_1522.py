# Generated by Django 3.1.3 on 2020-12-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyDoc', '0062_auto_20201212_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userappointment',
            name='date',
            field=models.DateTimeField(help_text='Date of scheduled appointment'),
        ),
        migrations.AlterField(
            model_name='userappointment',
            name='patient_name',
            field=models.CharField(help_text="The user selected above names';'", max_length=60, null=True),
        ),
    ]
