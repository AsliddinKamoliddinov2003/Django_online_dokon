from django import forms
from django.forms import fields

from .models import  News, Director, Filial


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        exclude = ['views']


    def __init__(self, *args, **kwargs):
        super(NewsForm,self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ["fullname", "experience","age", "image"]

    def __init__(self, *args, **kwargs):
        super(DirectorForm,self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"



class FilialForm(forms.ModelForm):
    established_at = forms.DateTimeField(input_formats=["%d.%m.%Y %H:%M"])
    class Meta:
        model = Filial
        fields = ["title", "established_at"]

    def __init__(self, *args, **kwargs):
        super(FilialForm,self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"



