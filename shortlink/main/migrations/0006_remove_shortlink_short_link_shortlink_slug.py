# Generated by Django 4.0.6 on 2022-07-09 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_shortlink_full_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shortlink',
            name='short_link',
        ),
        migrations.AddField(
            model_name='shortlink',
            name='slug',
            field=models.CharField(blank=True, max_length=28, unique=True, verbose_name='Сокращенная ссылка'),
        ),
    ]
