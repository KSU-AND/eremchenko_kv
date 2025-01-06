from django import forms 

from ..models.theory import TheoryBlock
from ..models.language import Language
from ..forms.widgets import textarea_hidden_widget, languages_widget


class TheoryTitleForm(forms.ModelForm):
    class Meta:
        model = TheoryBlock
        fields = ['title']
        labels = {'title': ''}
        widgets = {'title': textarea_hidden_widget}

class TheoryOutlineForm(forms.ModelForm):
    class Meta:
        model = TheoryBlock
        fields = ['outline']
        labels = {'outline': ''}
        widgets = {'outline': textarea_hidden_widget}

class TheoryTextForm(forms.ModelForm):
    class Meta:
        model = TheoryBlock
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': textarea_hidden_widget}

class LanguageForm(forms.ModelForm):
    class Meta:
        model = TheoryBlock
        fields = ['languages']
        labels = {'languages': ''}
        widgets = {'languages': languages_widget}
    