# Generated by Django 3.2.5 on 2021-07-17 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('type', models.CharField(choices=[('cake', 'Cake'), ('buscuit', 'Buscuit')], max_length=10)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
