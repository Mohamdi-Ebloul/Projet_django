# Generated by Django 4.0 on 2022-01-21 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0008_fournisseur_abrevation_fournisseur_domaine_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utlisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('address', models.EmailField(max_length=220)),
                ('login', models.CharField(max_length=220)),
                ('Password', models.IntegerField()),
                ('Type', models.CharField(max_length=220)),
                ('Stock', models.CharField(max_length=220)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
