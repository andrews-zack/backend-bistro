# Generated by Django 4.1.3 on 2022-11-11 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_bistro', '0003_rename_label_category_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='menuitem',
            old_name='cuisine_id',
            new_name='cuisine',
        ),
    ]