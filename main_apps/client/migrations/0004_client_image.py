# Generated by Django 4.2.6 on 2023-11-29 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_rename_resevation_reservation_alter_client_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='image',
            field=models.ImageField(default=1, upload_to='image/'),
            preserve_default=False,
        ),
    ]
