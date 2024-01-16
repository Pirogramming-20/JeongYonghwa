# Generated by Django 5.0.1 on 2024-01-16 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devtool', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devtool',
            name='explanation',
        ),
        migrations.RemoveField(
            model_name='devtool',
            name='tool_type',
        ),
        migrations.AddField(
            model_name='devtool',
            name='content',
            field=models.TextField(default='default', verbose_name='설명'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='devtool',
            name='kind',
            field=models.CharField(default='default', max_length=20, verbose_name='종류'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='devtool',
            name='name',
            field=models.CharField(max_length=20, verbose_name='이름'),
        ),
    ]
