# Generated by Django 4.2 on 2023-06-16 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_remove_customer_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date_of_birth',
            field=models.DateField(default='2001-01-01'),
            preserve_default=False,
        ),
    ]