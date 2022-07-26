# Generated by Django 4.0.3 on 2022-08-28 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_healthinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(default='', max_length=200, null=True)),
                ('food_type', models.CharField(default='', max_length=200, null=True)),
                ('food_quantity', models.CharField(default='', max_length=200, null=True)),
                ('food_unit', models.CharField(default='', max_length=200, null=True)),
                ('calories', models.CharField(default='', max_length=200, null=True)),
                ('update_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
