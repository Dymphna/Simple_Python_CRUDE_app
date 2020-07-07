from django import forms
from .models import Crude


class CrudeForm(forms.ModelForm):
    class Meta:
        model = Crude
        fields = ['name', 'subject', 'score']
