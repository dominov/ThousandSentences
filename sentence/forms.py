from django import forms

from sentence.models import Sentence


class SentenceForm(forms.ModelForm):
    class Meta:
        model = Sentence
        fields = '__all__'
        widgets = {
            'topic': forms.Select(attrs={'class': 'form-control'}),
            'keywords': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'keywords'}),
            'phrase_english': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'phrase_spanish': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'difficulty': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'difficulty'}),
        }
        labels = {
            'keywords': '', 'difficulty': '', 'content': ''
        }
