# Generated by Django 4.2 on 2023-04-22 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branch', '0001_initial'),
        ('bill', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sc_no', models.IntegerField()),
                ('full_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(blank=True, max_length=20, null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branch.branch')),
                ('demand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bill.demandtype')),
            ],
        ),
    ]
