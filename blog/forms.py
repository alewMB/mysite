from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
    
    # overriding default form setting and adding bootstrap class
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'placeholder': 'Nom *','class':'form-control'}
        self.fields['email'].widget.attrs = {'placeholder': 'Email *', 'class':'form-control'}
        self.fields['body'].widget.attrs = {'placeholder': 'Commentez içi...', 'class':'form-control', 'rows':'5'}
