from django.db import models

class Session(models.Model):
    movie = models.CharField(max_length=255)
    hall = models.CharField(max_length=100, default="Основной зал")
    date_time = models.CharField(max_length=100, default="2026-06-01T18:00:00Z")
    seats = models.IntegerField(default=50)

    def __str__(self):
        return f"{self.movie} ({self.hall})"

class Ticket(models.Model):
    session = models.ForeignKey(Session, related_name='tickets', on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    customer = models.CharField(max_length=255)

    def __str__(self):
        return f"Билет №{self.seat_number} на сеанс {self.session.id} для {self.customer}"