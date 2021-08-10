from django import forms
from django.forms import fields

from .models import *


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        exclude = ['views']


    def __init__(self, *args, **kwargs):
        super(NewsForm,self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"

