# Generated by Django 4.2.1 on 2023-08-27 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessprofile',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='business_logos/'),
        ),
    ]
