
from django import forms
from .models import movielist
class movieform(forms.ModelForm):
    class Meta:
        model= movielist
        fields=['name', 'desc', 'year']
