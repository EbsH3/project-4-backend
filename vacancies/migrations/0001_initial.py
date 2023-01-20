# Generated by Django 4.1.5 on 2023-01-20 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=700)),
                ('employer', models.ManyToManyField(related_name='vacancies', to='employers.employer')),
            ],
        ),
    ]
