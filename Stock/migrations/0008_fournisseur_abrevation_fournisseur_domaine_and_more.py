# Generated by Django 4.0 on 2022-01-21 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0007_alter_sorti_designation_alter_stock_qten_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fournisseur',
            name='Abrevation',
            field=models.CharField(default=3, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='Domaine',
            field=models.CharField(default=9, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='Email',
            field=models.CharField(default=8, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='Nif',
            field=models.IntegerField(default=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='NomDirecteur',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='RC',
            field=models.IntegerField(default=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='Tel',
            field=models.IntegerField(default=7),
            preserve_default=False,
        ),
    ]
