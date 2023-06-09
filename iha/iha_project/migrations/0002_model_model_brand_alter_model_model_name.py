# Generated by Django 4.2 on 2023-04-25 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iha_project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='model_brand',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='iha_project.brand', verbose_name='Model'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='model',
            name='model_name',
            field=models.CharField(max_length=100, verbose_name='Model Adı'),
        ),
    ]
