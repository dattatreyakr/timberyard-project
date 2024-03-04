# Generated by Django 4.0.4 on 2022-08-24 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderConfirm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(max_length=3000)),
                ('city', models.TextField(max_length=3000)),
                ('pin', models.IntegerField(max_length=3000)),
                ('phone', models.IntegerField(max_length=3000)),
                ('totalc', models.IntegerField(max_length=3000)),
                ('mode', models.TextField(max_length=3000)),
                ('date', models.DateTimeField(auto_now=True)),
                ('product', models.TextField(max_length=200)),
                ('product_id', models.TextField(max_length=200)),
                ('total_amount', models.IntegerField()),
                ('quantiy', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='woods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemAdded', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='woodImage/')),
                ('name', models.TextField(max_length=10000)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='benifits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benift', models.TextField(max_length=5000)),
                ('fkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.woods')),
            ],
        ),
    ]