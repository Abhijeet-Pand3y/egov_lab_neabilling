# Generated by Django 4.2 on 2023-06-16 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_payment_payment_option_alter_payment_fine_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentoption',
            name='name',
            field=models.CharField(choices=[('cash', 'cash'), ('Khalti', 'Khalti'), ('eSewa', 'eSewa'), ('fone pay', 'fone pay')], max_length=100),
        ),
    ]