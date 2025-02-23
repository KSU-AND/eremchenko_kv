from django import forms 

from ..models.language import Language
from .widgets import intable_select_widget


class AreaForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['area']
        labels = {'area': ''}
        widgets = {'area': intable_select_widget}
