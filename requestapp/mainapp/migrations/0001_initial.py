# Generated by Django 3.1.4 on 2020-12-19 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='ФИО')),
                ('phone', models.CharField(max_length=16, verbose_name='Номер телефона')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='ФИО')),
                ('position', models.CharField(max_length=128, verbose_name='Должность')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('text', models.TextField(verbose_name='Текст запроса')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.client')),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.employee')),
            ],
        ),
    ]