from django import forms 

from ..models.source import Source
from ..forms.widgets import source_widget


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ['source']
        labels = {'source': ''}
        widgets = {'source': source_widget}
