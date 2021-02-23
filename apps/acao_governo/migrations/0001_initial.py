# Generated by Django 3.1.5 on 2021-01-31 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcaoGoverno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('descricao', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
