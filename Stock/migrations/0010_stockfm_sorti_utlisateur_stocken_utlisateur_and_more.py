# Generated by Django 4.0 on 2022-01-21 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0009_utlisateur'),
    ]

    operations = [
        migrations.CreateModel(
            name='STOCKfm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Designation', models.CharField(max_length=30)),
                ('QTEx', models.IntegerField(default=0)),
                ('QTEn', models.IntegerField(default=0)),
                ('QTS', models.IntegerField(default=0)),
                ('QTR', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='sorti',
            name='Utlisateur',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Stock.utlisateur'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stocken',
            name='Utlisateur',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Stock.utlisateur'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='StockEnfm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QTEx', models.IntegerField()),
                ('QTEn', models.IntegerField()),
                ('QTR', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('Designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stock.stockfm')),
                ('Fournisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stock.fournisseur')),
                ('Stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stock.stock')),
                ('Utlisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stock.utlisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Sortifm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QTEx', models.IntegerField()),
                ('QTS', models.IntegerField()),
                ('QTR', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('Designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stock.stockfm')),
                ('Service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stock.service')),
                ('Utlisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stock.utlisateur')),
            ],
        ),
    ]
