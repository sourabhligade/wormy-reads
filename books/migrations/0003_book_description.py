# Generated by Django 4.2.7 on 2024-01-02 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_review_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='No description available'),
            preserve_default=False,
        ),
    ]
