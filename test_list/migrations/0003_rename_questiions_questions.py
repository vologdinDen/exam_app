# Generated by Django 4.0.3 on 2022-03-07 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_list', '0002_alter_questiions_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='questiions',
            new_name='questions',
        ),
    ]
