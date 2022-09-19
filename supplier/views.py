from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect
from api.create_files_api import create_compare_price, create_compare_series
from api.import_api import import_file
from utils.files import file_name_with_ext


