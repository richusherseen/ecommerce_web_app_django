# Generated by Django 2.1.7 on 2021-01-03 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_productmodel_offer_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='discount_amount',
            new_name='offer',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='offer_name',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='offer_start',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='vendor',
        ),
        migrations.AddField(
            model_name='offer',
            name='offer_type',
            field=models.CharField(choices=[('Percentage Offer', 'Percentage Offer'), ('Price Offer', 'Price Offer')], default='Price Offer', max_length=220),
        ),
    ]
