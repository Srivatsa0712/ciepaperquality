# Generated by Django 4.0.5 on 2022-10-09 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dept', '0007_cndisplay_iotdisplay_mldisplay_wsdisplay'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cndisplay',
            old_name='comments',
            new_name='comments_cn',
        ),
        migrations.RenameField(
            model_name='iotdisplay',
            old_name='comments',
            new_name='comments_iot',
        ),
        migrations.RenameField(
            model_name='mldisplay',
            old_name='comments',
            new_name='comments_ml',
        ),
        migrations.RenameField(
            model_name='wsdisplay',
            old_name='comments',
            new_name='comments_ws',
        ),
    ]
