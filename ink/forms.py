from .models import *
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField


class SummerForm(forms.Form):

    summer_form = forms.CharField(widget=SummernoteInplaceWidget())

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            'title', 'excerpt', 'content',
            'featured_image', 'status',
        )
        widget = {
            'content' : SummernoteWidget(),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('commented_text',)
