from django import forms
from .models import Note
from taggit.forms import TagWidget

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Title'}),
            'tags': TagWidget(attrs={'class': 'custom-input', 'placeholder': 'Enter tags seperated by commas'}),
        }
