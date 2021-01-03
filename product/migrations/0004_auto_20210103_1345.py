# Generated by Django 2.1.7 on 2021-01-03 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210103_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferByCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_type', models.CharField(choices=[('Price Offer', 'Price Offer'), ('Percentage Offer', 'Percentage Offer')], default='Price Offer', max_length=220)),
                ('offer', models.FloatField(null=True)),
                ('offer_expiry', models.DateField(null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.CategoryModel')),
            ],
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_type',
            field=models.CharField(choices=[('Price Offer', 'Price Offer'), ('Percentage Offer', 'Percentage Offer')], default='Price Offer', max_length=220),
        ),
    ]
