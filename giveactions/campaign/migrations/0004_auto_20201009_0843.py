# Generated by Django 3.1.2 on 2020-10-09 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0003_auto_20201006_1240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='nom',
            new_name='name',
        ),
    ]
