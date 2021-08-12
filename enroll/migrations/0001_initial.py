# Generated by Django 3.2.6 on 2021-08-09 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pan', models.CharField(max_length=100)),
                ('age', models.IntegerField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]
