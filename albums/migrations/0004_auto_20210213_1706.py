# Generated by Django 3.1.5 on 2021-02-13 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_auto_20210213_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image_url',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='albums.album'),
        ),
    ]
