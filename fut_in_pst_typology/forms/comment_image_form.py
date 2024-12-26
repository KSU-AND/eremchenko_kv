from django import forms 

from ..models.comment_image import CommentImage


class CommentImageForm(forms.ModelForm):
    class Meta:
        model = CommentImage
        fields = ['image']
        labels = {'image': ''}