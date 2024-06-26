# Generated by Django 5.0.4 on 2024-04-21 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_vacancy_game_alter_game_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='address',
        ),
        migrations.RemoveField(
            model_name='company',
            name='city',
        ),
        migrations.RemoveField(
            model_name='game',
            name='salary',
        ),
        migrations.AddField(
            model_name='company',
            name='financial_information',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='company',
            name='founded',
            field=models.CharField(default='2024-04-23', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='partners_and_investors',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='financial_results',
            field=models.FloatField(default='0.0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.CharField(default='Unknown', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='platforms',
            field=models.CharField(default='Unknown', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='relase_date',
            field=models.DateField(default='2024-04-23'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='reviews_and_ratings',
            field=models.CharField(default='Unknown', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='sales',
            field=models.FloatField(default='0.0'),
            preserve_default=False,
        ),
    ]
