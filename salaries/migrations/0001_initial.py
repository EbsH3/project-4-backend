# Generated by Django 4.1.5 on 2023-01-20 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sectors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('level_of_experience', models.CharField(max_length=50)),
                ('salary_benchmark', models.CharField(max_length=200)),
                ('sector', models.ManyToManyField(related_name='salaries', to='sectors.sector')),
            ],
        ),
    ]
