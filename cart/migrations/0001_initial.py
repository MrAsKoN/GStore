# Generated by Django 2.2.5 on 2019-11-03 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0005_customuser_address'),
        ('home', '0007_auto_20191103_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_ordered', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('date_ordered', models.DateTimeField(null=True)),
                ('product', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(max_length=15)),
                ('is_ordered', models.BooleanField(default=False)),
                ('date_ordered', models.DateTimeField(auto_now=True)),
                ('items', models.ManyToManyField(to='cart.OrderItem')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.CustomUser')),
            ],
        ),
    ]
