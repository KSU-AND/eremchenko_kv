from django.db import models

class Genus(models.Model):
    class Meta:
        verbose_name = "Род"
        verbose_name_plural = "Рода"

    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name