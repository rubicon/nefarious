# Generated by Django 3.0.2 on 2021-06-10 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nefarious', '0062_nefarioussettings_open_subtitles_auto'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='watchtvepisode',
            index=models.Index(fields=['season_number'], name='nefarious_w_season__72f942_idx'),
        ),
        migrations.AddIndex(
            model_name='watchtvepisode',
            index=models.Index(fields=['episode_number'], name='nefarious_w_episode_61846e_idx'),
        ),
        migrations.AddIndex(
            model_name='watchtvseason',
            index=models.Index(fields=['season_number'], name='nefarious_w_season__ee0cf5_idx'),
        ),
        migrations.AddIndex(
            model_name='watchtvseasonrequest',
            index=models.Index(fields=['collected'], name='nefarious_w_collect_cda148_idx'),
        ),
    ]
