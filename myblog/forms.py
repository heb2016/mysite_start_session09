from django import forms
from django.forms import Textarea

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        widgets = {
            'text': Textarea(attrs={'size': 10, 'title': 'Blog Title'})
        }