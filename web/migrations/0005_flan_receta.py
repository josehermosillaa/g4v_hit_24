# Generated by Django 4.2 on 2024-05-10 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='receta',
            field=models.TextField(default='Sin Receta'),
            preserve_default=False,
        ),
    ]