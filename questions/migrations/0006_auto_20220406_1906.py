# Generated by Django 2.2.19 on 2022-04-06 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20220405_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='text',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.BooleanField(default=False, verbose_name='Ответы'),
        ),
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.CharField(default=1, max_length=150, verbose_name='Текст вопроса'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
