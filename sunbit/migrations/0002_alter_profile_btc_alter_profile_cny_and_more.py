# Generated by Django 4.2.5 on 2023-09-23 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunbit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='btc',
            field=models.CharField(default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cny',
            field=models.CharField(default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='eth',
            field=models.CharField(default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='eur',
            field=models.CharField(default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gbp',
            field=models.CharField(default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hkd',
            field=models.CharField(default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='jpy',
            field=models.CharField(default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='usd',
            field=models.CharField(default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='usdc',
            field=models.CharField(default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='usdt',
            field=models.CharField(default=0, max_length=200, null=True),
        ),
    ]
