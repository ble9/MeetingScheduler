# Generated by Django 3.0.2 on 2020-03-10 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0008_auto_20200305_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeavailability',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='meeting.Profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='timeavailability',
            name='meeting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meeting.Meeting'),
        ),
    ]
