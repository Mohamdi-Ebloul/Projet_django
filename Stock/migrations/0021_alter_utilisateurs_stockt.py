# Generated by Django 4.0 on 2022-01-29 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0020_stockt_remove_stockenfm_designation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateurs',
            name='STOCKT',
            field=models.CharField(max_length=220),
        ),
    ]
