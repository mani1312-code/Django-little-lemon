# Generated by Django 4.2.5 on 2023-12-01 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_menu_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='description',
            new_name='menu_item_description',
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
