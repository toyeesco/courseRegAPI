# Generated by Django 5.0 on 2024-01-17 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_dean_name_hod_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dean',
            name='signature',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='hod',
            name='signature',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='reg_officer',
            name='signature',
            field=models.ImageField(upload_to='images'),
        ),
    ]