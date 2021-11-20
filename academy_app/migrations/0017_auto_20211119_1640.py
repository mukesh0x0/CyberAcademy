# Generated by Django 3.2.9 on 2021-11-19 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy_app', '0016_alter_curriculum_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curriculum',
            name='course',
        ),
        migrations.AddField(
            model_name='curriculumsubtopic',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='academy_app.courses', verbose_name='course_name'),
        ),
    ]
