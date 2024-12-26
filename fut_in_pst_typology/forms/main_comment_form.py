from django import forms 

from ..models.language import Language
from ..forms.widgets import main_comment_widget


class MainCommentForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['main_comment']
        labels = {'main_comment': ''}
        widgets = {'main_comment': main_comment_widget}
