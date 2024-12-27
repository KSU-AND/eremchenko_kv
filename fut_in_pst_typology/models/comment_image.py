from django.db import models

from .comment import Comment


class CommentImage(models.Model):
    class Meta:
        verbose_name = "Изображение комментария"
        verbose_name_plural = "Изображения комментариев"

    
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="comment_images/")