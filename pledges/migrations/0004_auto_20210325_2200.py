# Generated by Django 3.1.7 on 2021-03-25 22:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pledges', '0003_auto_20210325_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='answer',
            name='response_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='response_select',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pledges.select'),
        ),
    ]
