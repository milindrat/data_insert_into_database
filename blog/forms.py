from django import forms
from . models import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class Batch_expirationForm(forms.ModelForm):
    class Meta:
        model = Batch_expiration
        fields = '__all__'

class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields='__all__'

class OrdersToReceiveForm(forms.ModelForm):
    class Meta:
        model=OrdersToReceive
        fields='__all__'

class SalesHistoryForm(forms.ModelForm):
    class Meta:
        model=SalesHistory
        fields='__all__'        


class BatchExpirationUploadFileForm(forms.Form):
    file = forms.FileField()

class ItemUploadFileForm(forms.Form):
    file = forms.FileField()

class OrdersToReceiveUploadFileForm(forms.Form):
    file = forms.FileField()

class SalesHistoryUploadFileForm(forms.Form):
    file = forms.FileField()