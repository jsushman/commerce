# Generated by Django 3.1.3 on 2022-02-07 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20220207_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator', to='auctions.listing'),
        ),
        migrations.AlterField(
            model_name='user',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='top', to='auctions.listing'),
        ),
    ]
