from django.db import models

class Session(models.Model):
    movie = models.CharField(max_length=255)
    hall = models.CharField(max_length=100, default="Основной зал")
    date_time = models.CharField(max_length=100, default="2026-06-01T18:00:00Z")
    seats = models.IntegerField(default=50)

    def __str__(self):
        return f"{self.movie} ({self.hall})"