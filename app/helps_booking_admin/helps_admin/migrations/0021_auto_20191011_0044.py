# Generated by Django 2.2.4 on 2019-10-10 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helps_admin', '0020_auto_20191011_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffaccount',
            name='first_name',
            field=models.CharField(default='placeholder', max_length=30, null=True),
        ),
    ]
