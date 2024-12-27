from django.db import models

class Family(models.Model):
    class Meta:
        verbose_name = "Семья"
        verbose_name_plural = "Семьи"

    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name