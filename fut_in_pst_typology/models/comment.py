from django.db import models

from .language import Language

class Comment(models.Model):
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    comment = models.TextField()
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.comment[:20]