# Generated by Django 3.1.7 on 2021-03-25 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pledges', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='quextion_text',
            new_name='question_text',
        ),
        migrations.RemoveField(
            model_name='action',
            name='question_text',
        ),
    ]
