# Generated by Django 4.1.7 on 2023-05-07 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
