# Generated by Django 2.2.4 on 2019-10-10 13:46

from django.db import migrations, models
import helps_admin.models


class Migration(migrations.Migration):

    dependencies = [
        ('helps_admin', '0021_auto_20191011_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffaccount',
            name='DOB',
            field=models.DateField(default=helps_admin.models.default_start_time, null=True),
        ),
        migrations.AlterField(
            model_name='staffaccount',
            name='session_history',
            field=helps_admin.models.DateListField(default=helps_admin.models.default_start_time, null=True),
        ),
    ]
