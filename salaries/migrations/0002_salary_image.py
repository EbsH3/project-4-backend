# Generated by Django 4.1.5 on 2023-01-23 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salaries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='image',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]