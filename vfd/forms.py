from django import forms

from vfd.models import Supplier, Series


class SimpleUploadFileForm(forms.Form):
    file = forms.FileField()


# CREATE FILES #

class CreateComparePriceForm(forms.Form):
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all())
    series = forms.ModelMultipleChoiceField(queryset=Series.objects.all())


class CompareSeries(forms.Form):
    series = forms.ModelMultipleChoiceField(queryset=Series.objects.all())

    def __init__(self, *args, **kwargs):
        super(CompareSeries, self).__init__(*args, **kwargs)
        self.fields['series'].widget.attrs['size'] = 30
