from django.db import models

class Area(models.Model):
    class Meta:
        verbose_name = "Макро-ареал"
        verbose_name_plural = "Макро-ареалы"

    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name