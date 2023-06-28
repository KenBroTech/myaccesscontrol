from django import forms
from . models import CaesarEncrypt, cautionModel


class CaesarEncryptForm(forms.ModelForm):
    class Meta:
        fields = ['message', 'key']
        model = CaesarEncrypt


# class AESEncryptForm(forms.ModelForm):
#     class Meta:
#         fields = ['message']
#         model = AESEncrypt

class cautionModelForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'number']
        model = cautionModel