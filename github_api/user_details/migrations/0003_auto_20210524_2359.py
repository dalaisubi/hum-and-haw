# Generated by Django 3.0.5 on 2021-05-24 23:59

from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0002_auto_20210524_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reposdetail',
            name='repo',
            field=djongo.models.fields.JSONField(),
        ),
    ]