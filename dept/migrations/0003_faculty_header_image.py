# Generated by Django 4.0.5 on 2022-10-02 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dept', '0002_emf'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]