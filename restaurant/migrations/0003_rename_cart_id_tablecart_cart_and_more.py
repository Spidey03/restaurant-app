# Generated by Django 4.0.5 on 2022-06-11 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_item_description_item_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tablecart',
            old_name='cart_id',
            new_name='cart',
        ),
        migrations.RenameField(
            model_name='tablecart',
            old_name='table_id',
            new_name='table',
        ),
        migrations.RenameField(
            model_name='tablecart',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='tableorder',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='tableorder',
            old_name='table_id',
            new_name='table',
        ),
        migrations.RenameField(
            model_name='tableorder',
            old_name='user_id',
            new_name='user',
        ),
    ]