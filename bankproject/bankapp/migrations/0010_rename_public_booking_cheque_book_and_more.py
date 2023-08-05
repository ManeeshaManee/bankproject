# Generated by Django 4.1.5 on 2023-08-03 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0009_booking_public_alter_booking_date_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='public',
            new_name='CHEQUE_BOOK',
        ),
        migrations.AddField(
            model_name='booking',
            name='CREDIT_CARD',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='DEBIT_CARD',
            field=models.BooleanField(default=True),
        ),
    ]