# Generated by Django 3.1.4 on 2020-12-13 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organiser', '0004_auto_20201213_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savelink_org',
            name='labels',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='savelink_org',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='savelink_org',
            name='url',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
