# Generated by Django 2.2.2 on 2019-07-02 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0096_auto_20190702_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Max_Price',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='Color',
            field=models.TextField(blank=True),
        ),
    ]
