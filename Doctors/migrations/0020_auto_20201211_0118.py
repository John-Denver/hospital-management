# Generated by Django 3.1.3 on 2020-12-10 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0019_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='age',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='gender',
        ),
        migrations.DeleteModel(
            name='DoctAppointment',
        ),
    ]
