# Generated by Django 3.2.18 on 2023-04-25 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iha_project', '0006_rename_brand_name_brand_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='iha',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='model',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]