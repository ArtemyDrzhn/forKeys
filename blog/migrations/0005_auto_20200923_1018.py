# Generated by Django 2.2.16 on 2020-09-23 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200919_1322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='categories',
            new_name='name_cat',
        ),
    ]
