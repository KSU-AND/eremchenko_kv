from django.db import models


class TheoryBlock(models.Model):
    class Meta:
        verbose_name = "Теоретический блок"
        verbose_name_plural = "Теоретический блок"
    
    title = models.CharField(max_length=128)
    outline = models.TextField(blank=True)
    text = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.title