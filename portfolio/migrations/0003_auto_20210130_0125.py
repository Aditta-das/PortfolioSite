# Generated by Django 3.1.2 on 2021-01-29 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210130_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='colab',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='github',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='kaggle',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
