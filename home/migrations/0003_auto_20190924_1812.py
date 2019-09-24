# Generated by Django 2.2.5 on 2019-09-24 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190921_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date_added',
        ),
        migrations.AddField(
            model_name='product',
            name='avg_rating',
            field=models.FloatField(default=0.0, max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(default='Hardware', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
