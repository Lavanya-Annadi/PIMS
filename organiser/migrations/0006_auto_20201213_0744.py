# Generated by Django 3.1.4 on 2020-12-13 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organiser', '0005_auto_20201213_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savelink_org',
            name='read_status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='savelink_org',
            name='score',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='savelink_org',
            name='tags',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
