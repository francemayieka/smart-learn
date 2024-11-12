# Generated by Django 5.1.3 on 2024-11-12 18:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0003_exam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='course',
            name='last_updated',
        ),
        migrations.AddField(
            model_name='course',
            name='uploaded_file',
            field=models.FileField(blank=True, upload_to='course_outlines/'),
        ),
        migrations.AddField(
            model_name='exam',
            name='exam_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_outline',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='exam',
            name='marking_scheme',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='number_of_questions',
            field=models.IntegerField(default=0),
        ),
    ]
