# Generated by Django 4.2 on 2023-06-16 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0006_alter_bill_bill_amount_alter_bill_bill_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
    ]
