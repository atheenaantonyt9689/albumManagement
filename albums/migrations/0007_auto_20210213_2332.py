# Generated by Django 3.1.5 on 2021-02-13 18:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0006_album_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='datetime',
            new_name='posted_at',
        ),
        migrations.RemoveField(
            model_name='album',
            name='image_url',
        ),
        migrations.AddField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(null=True,blank=True,on_delete=django.db.models.deletion.CASCADE, to='albums.album'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='image_url',
            field=models.CharField(max_length=200),
        ),
    ]
