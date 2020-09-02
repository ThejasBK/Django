# Generated by Django 3.0.3 on 2020-08-11 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('user_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=264)),
                ('tz', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityPeriods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.UserInformation')),
            ],
        ),
    ]
