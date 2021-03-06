# Generated by Django 2.0.3 on 2018-05-12 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('name', models.CharField(default='', max_length=200, null=True)),
                ('release_date', models.DateTimeField(null=True)),
                ('game_category', models.CharField(default='', max_length=200, null=True)),
                ('played', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
