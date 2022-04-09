# Generated by Django 2.2.19 on 2022-04-08 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0011_auto_20220406_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='vote',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='questions.Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='test_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='questions.Test'),
        ),
    ]
