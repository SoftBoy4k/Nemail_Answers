from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': 'New question'}

class EntryForm(forms.ModelForm):
    
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgers = {'text': forms.Textarea(attrs={'cols': 80})}