# Generated by Django 3.2.9 on 2021-11-19 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy_app', '0014_rename_curriculumtopic_curriculumsubtopic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curriculumsubtopic',
            name='course',
        ),
        migrations.AddField(
            model_name='curriculum',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='academy_app.courses', verbose_name='course_name'),
        ),
    ]