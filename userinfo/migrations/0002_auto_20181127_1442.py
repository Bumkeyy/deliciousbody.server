# Generated by Django 2.1 on 2018-11-27 05:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='activity_level',
            field=models.IntegerField(default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)], verbose_name='활동 수준'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(default=25, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(200)], verbose_name='나이'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='프로필 사진'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='comment',
            field=models.CharField(blank=True, default='comment', max_length=30, verbose_name='동기 부여 멘트'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='favorite_list',
            field=models.CharField(default='1;2;3', max_length=1000, verbose_name='좋아요 리스트'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='interested_part',
            field=models.CharField(default='1;2;3', max_length=20, verbose_name='관심 부위'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='is_man',
            field=models.BooleanField(default=True, verbose_name='남자 유무'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='is_push_weekdays',
            field=models.BooleanField(default=True, verbose_name='주중 알림'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='is_push_weekend',
            field=models.BooleanField(default=True, verbose_name='주말 알림'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(blank=True, max_length=30, verbose_name='이름'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='weekdays_end',
            field=models.IntegerField(default=22, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)], verbose_name='주중 알림 종료 시간'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='weekdays_start',
            field=models.IntegerField(default=8, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)], verbose_name='주중 알림 시작 시간'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='weekend_end',
            field=models.IntegerField(default=22, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)], verbose_name='주말 알림 종료 시간'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='weekend_start',
            field=models.IntegerField(default=8, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)], verbose_name='주말 알림 시작 시간'),
        ),
    ]
