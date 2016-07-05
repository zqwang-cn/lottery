# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-06 00:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='FootballBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('comb_type', models.CharField(max_length=20)),
                ('bet_count', models.PositiveIntegerField(default=0)),
                ('match_count', models.PositiveSmallIntegerField()),
                ('finished_match_count', models.PositiveSmallIntegerField(default=0)),
                ('multiple', models.PositiveSmallIntegerField(default=1)),
                ('is_payed', models.BooleanField(default=0)),
                ('bonus', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('acct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Account')),
            ],
        ),
        migrations.CreateModel(
            name='FootballBillDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.FootballBill')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home', models.CharField(max_length=50)),
                ('away', models.CharField(max_length=50)),
                ('SN', models.CharField(max_length=10)),
                ('event', models.CharField(max_length=20)),
                ('time', models.DateTimeField()),
                ('handicap', models.CharField(max_length=3)),
                ('HAD', models.CharField(default=b'x', max_length=1)),
                ('HHAD', models.CharField(default=b'x', max_length=1)),
                ('CRS', models.CharField(default=b'x:x', max_length=5)),
                ('TTG', models.PositiveSmallIntegerField(default=0)),
                ('HFT', models.PositiveSmallIntegerField(default=0)),
                ('mcode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Odd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('odd', models.CharField(max_length=500)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.Match')),
            ],
        ),
        migrations.CreateModel(
            name='TraditionalBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=5)),
                ('multiple', models.PositiveSmallIntegerField(default=1)),
                ('content', models.CharField(max_length=115)),
                ('bet_count', models.PositiveIntegerField()),
                ('bonus', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('time', models.DateTimeField(auto_now=True)),
                ('is_payed', models.BooleanField(default=False)),
                ('acct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Account')),
            ],
        ),
        migrations.CreateModel(
            name='TraditionalGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SN', models.CharField(max_length=10)),
                ('deadline', models.DateTimeField()),
                ('results', models.CharField(default=b'x', max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='TraditionalMatches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.TraditionalGame')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.Match')),
            ],
        ),
        migrations.AddField(
            model_name='traditionalbill',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.TraditionalGame'),
        ),
        migrations.AddField(
            model_name='footballbilldetail',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.Match'),
        ),
        migrations.AddField(
            model_name='footballbilldetail',
            name='odd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.Odd'),
        ),
        migrations.AddField(
            model_name='currentmatch',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.Match'),
        ),
        migrations.AddField(
            model_name='currentmatch',
            name='odd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.Odd'),
        ),
    ]
