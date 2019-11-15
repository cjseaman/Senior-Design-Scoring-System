# Generated by Django 2.2.6 on 2019-11-14 04:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_site', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='Add Judge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='session',
            name='Add Student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_site.Student'),
        ),
    ]
