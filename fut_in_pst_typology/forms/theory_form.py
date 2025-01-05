from django import forms 

from ..models.theory import TheoryBlock
from ..forms.widgets import theory_title_widget, theory_text_widget, theory_outline_widget


class TheoryTitleForm(forms.ModelForm):
    class Meta:
        model = TheoryBlock
        fields = ['title']
        labels = {'title': ''}
        widgets = {'title': theory_title_widget}

class TheoryOutlineForm(forms.ModelForm):
    class Meta:
        model = TheoryBlock
        fields = ['outline']
        labels = {'outline': ''}
        widgets = {'outline': theory_outline_widget}

class TheoryTextForm(forms.ModelForm):
    class Meta:
        model = TheoryBlock
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': theory_text_widget}
