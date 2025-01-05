from django import forms
from .models import *

class Blog_form(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['text','photo']