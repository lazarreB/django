# Generated by Django 2.2.28 on 2023-04-24 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=6)),
            ],
        ),
    ]
