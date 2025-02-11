from django import forms 

from ..models.language import Language
from .widgets import intable_select_widget


class ProgressForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['progress']
        labels = {'progress': ''}
        widgets = {'progress': intable_select_widget}
