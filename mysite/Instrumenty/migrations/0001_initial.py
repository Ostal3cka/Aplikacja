# Generated by Django 4.0.3 on 2022-05-12 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Muzyk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rodzaj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=200, null=True)),
                ('opis', models.CharField(max_length=500, null=True)),
                ('muzyk', models.ManyToManyField(to='Instrumenty.muzyk')),
                ('rodzaj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Instrumenty.rodzaj')),
            ],
        ),
    ]
