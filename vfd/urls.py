from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index_view'),

    path('import/', import_files_view, name='import_files_view'),
]
