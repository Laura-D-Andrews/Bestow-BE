# Generated by Django 4.2.4 on 2023-08-28 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=300)),
                ('gender', models.CharField(max_length=300)),
                ('relationship', models.CharField(max_length=300)),
                ('price_range', models.CharField(max_length=300)),
                ('occasion', models.CharField(max_length=300)),
                ('gift_type', models.CharField(max_length=300)),
                ('interest', models.CharField(max_length=300)),
            ],
        ),
    ]
