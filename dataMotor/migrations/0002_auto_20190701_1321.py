# Generated by Django 2.0.6 on 2019-07-01 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataMotor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='motor',
            old_name='cc_mototr',
            new_name='cc_motor',
        ),
    ]
