# Generated by Django 3.1.5 on 2021-02-17 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('albums', '0010_auto_20210214_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='user',
            field=models.ForeignKey(null=True,blank=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
