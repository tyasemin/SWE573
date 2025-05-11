from django import forms
from db.models import Board

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'description'] 