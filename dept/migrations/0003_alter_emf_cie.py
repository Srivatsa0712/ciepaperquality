# Generated by Django 4.1 on 2022-09-21 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dept', '0002_emf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emf',
            name='cie',
            field=models.ImageField(upload_to='images'),
        ),
    ]