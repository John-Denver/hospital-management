# Generated by Django 3.1.3 on 2020-12-11 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0021_auto_20201211_1059'),
        ('MyDoc', '0058_auto_20201211_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medrecs',
            name='clinician',
        ),
        migrations.AddField(
            model_name='medrecs',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Doctors.doctor'),
        ),
    ]
