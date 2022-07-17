from django import forms

from vfd.models import Supplier, Series


class SimpleUploadFileForm(forms.Form):
    file = forms.FileField()


# CREATE FILES #

class CreateComparePriceForm(forms.Form):
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all())
    series = forms.ModelMultipleChoiceField(queryset=Series.objects.all())
