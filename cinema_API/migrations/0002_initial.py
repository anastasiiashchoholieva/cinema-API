# Generated by Django 4.2.1 on 2023-06-28 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cinema_API", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="moviesession",
            name="cinema_hall",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cinema_API.cinemahall"
            ),
        ),
        migrations.AddField(
            model_name="moviesession",
            name="movie",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cinema_API.movie"
            ),
        ),
        migrations.AddField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(blank=True, to="cinema_API.actor"),
        ),
        migrations.AddField(
            model_name="movie",
            name="genres",
            field=models.ManyToManyField(blank=True, to="cinema_API.genre"),
        ),
        migrations.AlterUniqueTogether(
            name="ticket",
            unique_together={("movie_session", "row", "seat")},
        ),
    ]