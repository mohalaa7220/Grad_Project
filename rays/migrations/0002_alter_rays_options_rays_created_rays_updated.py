# Generated by Django 4.1.5 on 2023-01-31 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rays', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rays',
            options={'verbose_name': 'Rays', 'verbose_name_plural': 'Rays'},
        ),
        migrations.AddField(
            model_name='rays',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='rays',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
