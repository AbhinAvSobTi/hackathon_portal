# Generated by Django 3.0.4 on 2020-04-02 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='member1_github',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
