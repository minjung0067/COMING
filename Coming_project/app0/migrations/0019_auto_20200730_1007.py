# Generated by Django 3.0.6 on 2020-07-30 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app0', '0018_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]