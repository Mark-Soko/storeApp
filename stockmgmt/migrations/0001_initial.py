# Generated by Django 2.2.13 on 2021-07-04 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.IntegerField(default='0', null=True)),
                ('receive_quantity', models.IntegerField(blank=True, default='0', null=True)),
                ('receive_by', models.CharField(blank=True, max_length=50, null=True)),
                ('issue_quantity', models.IntegerField(blank=True, default='0', null=True)),
                ('issue_by', models.CharField(blank=True, max_length=50, null=True)),
                ('issue_to', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('created_by', models.CharField(blank=True, max_length=50, null=True)),
                ('reorder_level', models.IntegerField(blank=True, default='0', null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('unit_buy_price', models.FloatField(blank=True, null=True)),
                ('unit_sell_price', models.FloatField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='stockmgmt.Category')),
            ],
        ),
    ]
