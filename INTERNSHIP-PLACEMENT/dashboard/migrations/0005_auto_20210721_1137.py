# Generated by Django 3.2.5 on 2021-07-21 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20210721_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='internshipinfo',
            old_name='company_name',
            new_name='company_username',
        ),
        migrations.RenameField(
            model_name='placementinfo',
            old_name='company_name',
            new_name='company_username',
        ),
    ]