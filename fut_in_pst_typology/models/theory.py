from django.db import models

from .language import Language


class TheoryBlock(models.Model):
    class Meta:
        verbose_name = "Теоретический блок"
        verbose_name_plural = "Теоретический блок"
    
    title = models.CharField(max_length=128)
    outline = models.TextField(blank=True)
    text = models.TextField(blank=True)
    languages = models.ManyToManyField(Language, related_name="theory_blocks")

    def __str__(self) -> str:
        return self.title