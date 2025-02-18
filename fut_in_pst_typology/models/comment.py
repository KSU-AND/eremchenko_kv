from django.db import models

from .language import Language
from accounts.models import User

def get_mendatsium():
    return User.objects.get(username="mendatsium").id

class Comment(models.Model):
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_mendatsium)
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.comment[:20]