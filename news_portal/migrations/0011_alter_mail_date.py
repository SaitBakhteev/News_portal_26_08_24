# Generated by Django 5.0.3 on 2024-08-21 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_portal', '0010_alter_mail_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
