# Generated by Django 3.2.4 on 2021-06-28 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0002_answers_vehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='inspection_type',
            field=models.TextField(null=True),
        ),
    ]