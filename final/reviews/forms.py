from django import forms
from .models import Category, Tag, Theme, Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'categories', 'tags', 'theme', 'content', 'image']
        widgets = {
            'tags': forms.TextInput(attrs={'placeholder': 'Enter comma-separated tags'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }

class ThemeCustomizationForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['name', 'slug', 'thumbnail']
