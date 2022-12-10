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


class AdressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["country", "city", "street", "building", "floor", "appertment", "pochta_code"]


    def __init__(self, *args, **kwargs):
        super(AdressForm,self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ["first_name", "last_name", "phone", "email", "address_line_1", "address_line_2", "country", "region", "city", "order_note"]