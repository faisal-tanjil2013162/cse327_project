# Generated by Django 4.0.3 on 2022-08-28 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_dietrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='dietrecord',
            name='apple_unit',
            field=models.CharField(choices=[('gram', 'gram'), ('liter', 'Lunch'), ('cup', 'cup'), ('piece', 'piece')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dietrecord',
            name='banana_unit',
            field=models.CharField(choices=[('gram', 'gram'), ('liter', 'Lunch'), ('cup', 'cup'), ('piece', 'piece')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dietrecord',
            name='beef_unit',
            field=models.CharField(choices=[('gram', 'gram'), ('liter', 'Lunch'), ('cup', 'cup'), ('piece', 'piece')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dietrecord',
            name='bread_unit',
            field=models.CharField(choices=[('gram', 'gram'), ('liter', 'Lunch'), ('cup', 'cup'), ('piece', 'piece')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dietrecord',
            name='broccoli_unit',
            field=models.CharField(choices=[('gram', 'gram'), ('liter', 'Lunch'), ('cup', 'cup'), ('piece', 'piece')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dietrecord',
            name='chicken_unit',
            field=models.CharField(choices=[('gram', 'gram'), ('liter', 'Lunch'), ('cup', 'cup'), ('piece', 'piece')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dietrecord',
            name='corn_unit',
            field=models.CharField(choices=[('gram', 'gram'), ('liter', 'Lunch'), ('cup', 'cup'), ('piece', 'piece')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dietrecord',
            name='fish_unit',
            field=models.CharField(choices=[('gram', 'gram'), ('liter', 'Lunch'), ('cup', 'cup'), ('piece', 'piece')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dietrecord',
            name='lantil_unit',
            field=models.CharField(choices=[('gram', 'gram'), ('liter', 'Lunch'), ('cup', 'cup'), ('piece', 'piece')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dietrecord',
            name='milk_unit',
            field=models.CharField(choices=[('gram', 'gram'), ('liter', 'Lunch'), ('cup', 'cup'), ('piece', 'piece')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dietrecord',
            name='mutton_unit',
            field=models.CharField(choices=[('gram', 'gram'), ('liter', 'Lunch'), ('cup', 'cup'), ('piece', 'piece')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dietrecord',
            name='orange_unit',
            field=models.CharField(choices=[('gram', 'gram'), ('liter', 'Lunch'), ('cup', 'cup'), ('piece', 'piece')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dietrecord',
            name='potatoes_unit',
            field=models.CharField(choices=[('gram', 'gram'), ('liter', 'Lunch'), ('cup', 'cup'), ('piece', 'piece')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dietrecord',
            name='rice_unit',
            field=models.CharField(choices=[('gram', 'gram'), ('liter', 'Lunch'), ('cup', 'cup'), ('piece', 'piece')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dietrecord',
            name='wheat_unit',
            field=models.CharField(choices=[('gram', 'gram'), ('liter', 'Lunch'), ('cup', 'cup'), ('piece', 'piece')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dietrecord',
            name='yogurt_unit',
            field=models.CharField(choices=[('gram', 'gram'), ('liter', 'Lunch'), ('cup', 'cup'), ('piece', 'piece')], max_length=100, null=True),
        ),
    ]