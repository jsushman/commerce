# Generated by Django 3.1.3 on 2021-01-07 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20210106_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='for_sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opinions', to='auctions.listing'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
