# Generated by Django 3.2.5 on 2021-08-06 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_companyuser_comimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyuser',
            name='comImage',
            field=models.ImageField(default='static/images/user_profile1.png', null=True, upload_to='Images/'),
        ),
    ]
