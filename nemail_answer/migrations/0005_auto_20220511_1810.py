# Generated by Django 3.2.13 on 2022-05-11 15:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nemail_answer', '0004_entry_owner'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Topic',
            new_name='Answer',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='topic',
            new_name='answer',
        ),
    ]
