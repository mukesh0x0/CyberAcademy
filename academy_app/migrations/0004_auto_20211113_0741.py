# Generated by Django 3.2.9 on 2021-11-13 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('academy_app', '0003_auto_20211112_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enroll',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='course',
        ),
        migrations.AddField(
            model_name='enroll',
            name='payment_id',
            field=models.IntegerField(default=None, null=True, verbose_name='payment id'),
        ),
        migrations.AddField(
            model_name='payment',
            name='course_id',
            field=models.IntegerField(default=None, verbose_name='course id'),
        ),
        migrations.AlterField(
            model_name='enroll',
            name='address',
            field=models.TextField(default=None, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='enroll',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy_app.courses', verbose_name='course'),
        ),
        migrations.AlterField(
            model_name='enroll',
            name='email',
            field=models.CharField(default=None, max_length=254, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='enroll',
            name='first_name',
            field=models.CharField(default=None, max_length=50, null=True, verbose_name='first'),
        ),
        migrations.AlterField(
            model_name='enroll',
            name='last_name',
            field=models.CharField(default=None, max_length=50, null=True, verbose_name='last'),
        ),
        migrations.AlterField(
            model_name='enroll',
            name='phone',
            field=models.CharField(default=None, max_length=50, null=True, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='enroll',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]