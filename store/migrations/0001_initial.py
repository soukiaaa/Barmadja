# Generated by Django 5.0.6 on 2024-07-23 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('isregistred', models.BooleanField(default=False)),
                ('datec', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['-designation'],
            },
        ),
        migrations.CreateModel(
            name='sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix', models.FloatField()),
                ('etat', models.CharField(choices=[('not yet', 'not yet'), ('in progress', 'in progress'), ('done', 'done')], default='not yet', max_length=50)),
                ('duree', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('simple', 'simple'), ('intermediate', 'intermediate'), ('professionnel', 'professionnel')], default='pose', max_length=50)),
                ('dated', models.DateField()),
                ('datef', models.DateField()),
                ('payer', models.CharField(max_length=20)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.client')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.project')),
            ],
            options={
                'ordering': ['-etat'],
            },
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.FloatField()),
                ('versement_date_time', models.DateTimeField(auto_now_add=True)),
                ('sales', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.sales')),
            ],
            options={
                'ordering': ['-sales'],
            },
        ),
        migrations.AddField(
            model_name='project',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.service'),
        ),
    ]
