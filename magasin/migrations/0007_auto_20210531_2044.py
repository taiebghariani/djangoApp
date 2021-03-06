# Generated by Django 3.2 on 2021-05-31 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0006_commande'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emballage',
            name='couleur',
            field=models.CharField(choices=[('bl', 'blanc'), ('rg', 'rouge'), ('ble', 'bleu'), ('vr', 'vert'), ('muli', 'multicolore')], default='Transparent', max_length=10),
        ),
        migrations.AlterField(
            model_name='produit',
            name='type',
            field=models.CharField(choices=[('em', 'emballé'), ('fr', 'frais'), ('cs', 'conserver')], default='em', max_length=2),
        ),
    ]
