# Generated by Django 3.2.9 on 2021-11-19 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy_app', '0010_alter_curriculum_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtopic',
            name='curriculum',
        ),
        migrations.AddField(
            model_name='curriculum',
            name='subtopic',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='academy_app.subtopic'),
        ),
    ]
