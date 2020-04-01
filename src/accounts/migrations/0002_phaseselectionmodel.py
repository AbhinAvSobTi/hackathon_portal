# Generated by Django 3.0.4 on 2020-03-29 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='phaseSelectionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section1', models.BooleanField(default=True)),
                ('section2', models.BooleanField(default=False)),
                ('section3', models.BooleanField(default=False)),
                ('section4', models.BooleanField(default=False)),
                ('final', models.BooleanField(default=False)),
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.team')),
            ],
        ),
    ]