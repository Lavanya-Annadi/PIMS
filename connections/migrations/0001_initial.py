# Generated by Django 3.1.4 on 2020-12-17 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='username', max_length=200)),
                ('connected_users', models.TextField()),
                ('pending_users', models.TextField()),
            ],
        ),
    ]
