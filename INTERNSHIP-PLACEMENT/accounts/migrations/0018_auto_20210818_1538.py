# Generated by Django 3.2.5 on 2021-08-18 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20210815_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyuser',
            name='password',
        ),
        migrations.RemoveField(
            model_name='studentuser',
            name='password',
        ),
        migrations.AlterField(
            model_name='companyuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]