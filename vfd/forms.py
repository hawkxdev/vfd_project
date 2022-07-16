from django import forms


class SimpleUploadFileForm(forms.Form):
    file = forms.FileField()
