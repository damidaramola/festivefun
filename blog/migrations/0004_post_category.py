# Generated by Django 3.2.20 on 2023-08-12 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Festivals', 'Festivals'), ('Clothing', 'Clothing'), ('Food', 'Food')], default='normal', max_length=50),
        ),
    ]
