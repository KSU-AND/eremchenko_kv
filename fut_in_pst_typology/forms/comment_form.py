from django import forms 

from ..models.comment import Comment
from ..forms.widgets import comment_widget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        labels = {'comment': ''}
        widgets = {'comment': comment_widget}