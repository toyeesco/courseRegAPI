# Generated by Django 5.0 on 2023-12-20 22:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0005_dean_name_hod_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('course_code', models.CharField(blank=True, choices=[('SEN401', 'SEN401'), ('SEN402', 'SEN402'), ('SEN403', 'SEN403'), ('SEN404', 'SEN404'), ('SEN405', 'SEN405'), ('SEN406', 'SEN406'), ('SEN407', 'SEN407'), ('SEN409', 'SEN409')], max_length=50)),
                ('course_unit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EnrollmentCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_at', models.DateField(auto_now=True)),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courses')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.student')),
            ],
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courses')),
                ('dean', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dean', to='authentication.dean')),
                ('enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.enrollmentcourse')),
                ('hod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hod', to='authentication.hod')),
                ('reg_officer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reg_officer', to='authentication.reg_officer')),
            ],
        ),
    ]
