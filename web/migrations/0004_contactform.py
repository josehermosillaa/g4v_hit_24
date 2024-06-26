# Generated by Django 4.2 on 2024-05-06 22:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0003_alter_flan_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactForm",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "contact_form_uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False),
                ),
                ("customer_email", models.EmailField(max_length=254)),
                ("customer_name", models.CharField(max_length=64)),
                ("message", models.TextField()),
            ],
        ),
    ]
