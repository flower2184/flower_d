from django import forms
from gameboard.models import Games, Answer
from django_summernote.widgets import SummernoteWidget

class GamesForm(forms.ModelForm):
    class Meta:
        model = Games
        fields = ['subject', 'content']
        widgets = {
            'content': SummernoteWidget(),
        }
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '내용',
        }