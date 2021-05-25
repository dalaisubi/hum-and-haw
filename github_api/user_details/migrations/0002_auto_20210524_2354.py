# Generated by Django 3.0.5 on 2021-05-24 23:54

from django.db import migrations, models
import django.utils.timezone
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='owner',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='reposdetail',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reposdetail',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='reposdetail',
            name='repo',
            field=djongo.models.fields.JSONField(default={}),
        ),
    ]