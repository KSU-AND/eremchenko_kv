from django import forms 

from ..models.language import Language
from ..forms.widgets import intable_select_widget


class MMForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['mm']
        labels = {'mm': ''}
        widgets = {'mm': intable_select_widget}

class MAForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['ma']
        labels = {'ma': ''}
        widgets = {'ma': intable_select_widget}

class AMForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['am']
        labels = {'am': ''}
        widgets = {'am': intable_select_widget}

class AAForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['aa']
        labels = {'aa': ''}
        widgets = {'aa': intable_select_widget}
