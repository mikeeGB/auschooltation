# Generated by Django 3.2.6 on 2021-09-05 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_alter_useranswer_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswer',
            name='question',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='quiz.question'),
            preserve_default=False,
        ),
    ]
