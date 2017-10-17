from django import forms

from .models import Comment


# Here I used fields inside The Comment Model Which I created in product/models
# Why I used Only body Field? Cuz We want only Users write Comments under Post
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

