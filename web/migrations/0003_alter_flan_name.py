# Generated by Django 4.2 on 2024-05-04 14:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0002_alter_flan_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flan",
            name="name",
            field=models.CharField(max_length=64),
        ),
    ]
