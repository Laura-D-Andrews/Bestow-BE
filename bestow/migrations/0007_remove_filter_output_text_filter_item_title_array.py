# Generated by Django 4.2.4 on 2023-11-01 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestow', '0006_remove_filter_test_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filter',
            name='output_text',
        ),
        migrations.AddField(
            model_name='filter',
            name='item_title_array',
            field=models.TextField(default=''),
        ),
    ]
