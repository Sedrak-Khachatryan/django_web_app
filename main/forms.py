from django import forms


class ContactFormBack(forms.Form):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

