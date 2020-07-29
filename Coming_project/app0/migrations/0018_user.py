# Generated by Django 3.0.8 on 2020-07-29 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app0', '0017_auto_20200726_0222'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='사용자명')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'db_table': 'test_user',
            },
        ),
    ]
