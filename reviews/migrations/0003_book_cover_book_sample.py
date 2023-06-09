# Generated by Django 4.1.7 on 2023-04-24 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_alter_book_id_alter_bookcontributor_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='post_covers/'),
        ),
        migrations.AddField(
            model_name='book',
            name='sample',
            field=models.FileField(blank=True, null=True, upload_to='post_samples/'),
        ),
    ]
