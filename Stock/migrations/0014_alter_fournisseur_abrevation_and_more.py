# Generated by Django 4.0 on 2022-01-24 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0013_admins_utilisateurs_user_remove_sortifm_utlisateur_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fournisseur',
            name='Abrevation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='fournisseur',
            name='Domaine',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='fournisseur',
            name='Nom',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='fournisseur',
            name='NomDirecteur',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stock',
            name='Designation',
            field=models.CharField(max_length=100),
        ),
    ]
