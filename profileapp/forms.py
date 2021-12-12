from django import forms

from .models import *



class ClientForm(forms.ModelForm):
    class Meta:
        model = ClientProfile
        fields = ["first_name", "last_name", "email", "image", "phone_number"]


    def __init__(self, *args, **kwargs):
        super(ClientForm,self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"