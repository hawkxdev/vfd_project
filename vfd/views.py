from django.shortcuts import render, redirect
from api.import_api import import_file
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
