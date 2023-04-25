# Generated by Django 4.2 on 2023-04-25 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='iha_project.brand', verbose_name='Model')),
            ],
        ),
        migrations.CreateModel(
            name='Iha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField(verbose_name='Ağırlık')),
                ('brand', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='iha_project.brand', verbose_name='Marka')),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='iha_project.category', verbose_name='Kategori')),
                ('model', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='iha_project.model', verbose_name='Model')),
            ],
        ),
    ]
