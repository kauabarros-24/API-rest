# Generated by Django 5.0.2 on 2024-03-17 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_livro"),
    ]

    operations = [
        migrations.AddField(
            model_name="livro",
            name="categoria",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
