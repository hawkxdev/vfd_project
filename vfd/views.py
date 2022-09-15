from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect
from api.create_files_api import create_compare_price, create_compare_series
from api.import_api import import_file
from utils.files import file_name_with_ext
from vfd import forms


def index_view(request):
    return render(request, 'vfd/index.html')


def handle_uploaded_file(folder, f):
    filename = f'{folder}/{f.name}'
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return filename


def import_files_view(request):
    if request.method == 'POST':
        form = forms.SimpleUploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filename = handle_uploaded_file('upload', request.FILES['file'])
            import_file(filename)
            return redirect('/import')
    else:
        form = forms.SimpleUploadFileForm()

    return render(request, 'vfd/import.html', {'form': form})


# CREATE FILES #

def create_compare_price_view(request):
    if request.method == 'POST':
        form = forms.CreateComparePriceForm(request.POST)
        if form.is_valid():
            supplier = request.POST.get('supplier', None)
            create_compare_price()
            return redirect('/create/compare-price/')
    else:
        form = forms.CreateComparePriceForm()

    return render(request, 'vfd/create/compare.html', {'form': form})


def compare_series(request):
    if request.method == 'POST':
        form = forms.CompareSeries(request.POST)
        if form.is_valid():
            series = request.POST.getlist('series')
            filename = create_compare_series(series)
            response = HttpResponse(open(filename, "rb"),
                                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename="{file_name_with_ext(filename)}"'
            return response
    else:
        form = forms.CompareSeries()

    return render(request, 'vfd/create/compare_series.html', {'form': form})
