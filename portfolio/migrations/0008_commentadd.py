# Generated by Django 3.1.2 on 2021-02-07 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20210201_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentAdd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('post_text', models.TextField()),
            ],
        ),
    ]