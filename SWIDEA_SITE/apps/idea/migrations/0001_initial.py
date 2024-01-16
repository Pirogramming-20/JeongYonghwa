# Generated by Django 5.0.1 on 2024-01-16 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('devtool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='아이디어명')),
                ('image', models.ImageField(null=True, upload_to='posts/', verbose_name='이미지')),
                ('explanation', models.CharField(max_length=255, verbose_name='아이디어 설명')),
                ('interest', models.IntegerField(default=0, verbose_name='아이디어 관심도')),
                ('devtool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devtool.devtool', verbose_name='예상 개발툴')),
            ],
        ),
    ]
