from django.db import models

from .language import Language


class Source(models.Model):
    class Meta:
        verbose_name = "Источник"
        verbose_name_plural = "Источники"

    source = models.CharField(max_length=400)
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.source
