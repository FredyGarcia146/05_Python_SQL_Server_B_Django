# Generated by Django 4.0.7 on 2022-09-14 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_postulants_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateChange',
            fields=[
                ('Id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('State_change', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='State_Change', max_length=12)),
                ('Date_change', models.DateTimeField(blank=True, db_column='Date_Change', null=True)),
                ('Description', models.CharField(blank=True, db_collation='Modern_Spanish_CI_AS', db_column='Description', max_length=100, null=True)),
            ],
            options={
                'db_table': 'State_Change',
                'managed': False,
            },
        ),
    ]
