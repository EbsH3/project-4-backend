# Generated by Django 4.1.5 on 2023-01-20 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('logo', models.CharField(max_length=700)),
            ],
        ),
    ]
