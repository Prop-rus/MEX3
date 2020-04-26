import mimetypes
import os
from threading import Thread, Timer
from django.http import request, HttpRequest, HttpResponseRedirect, HttpResponse, FileResponse
from django.shortcuts import render, redirect
from datetime import datetime

from MEX3.settings import MEDIA_ROOT, BASE_DIR
from .forms import InputFileForm
from .backend import handle_uploaded_file, form1Unit, deletefile


# Create your views here.

def Home_view(request):
    '''Renders home page'''
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        {
            'title': 'Make Excel',

            'year': datetime.now().year

        }
    )


def Form_view(request):
    '''Renders a page with first function '''

    if request.method == 'POST':
        os.chdir(BASE_DIR)
        form = InputFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('file')
        if form.is_valid():
            dir_path, extract_type = handle_uploaded_file(files)  # places uploaded files in tmp dir
            cellcomm = form.cleaned_data['column_comment'] + str(form.cleaned_data['row_comment'])
            cellvalue = form.cleaned_data['column_value'] + str(form.cleaned_data['row_value'])
            result_file = form1Unit(dir_path, extract_type, cellcomm, cellvalue)  # opens each file, combines and save result file

        return redirect('sendfile')


    else:
        form = InputFileForm()
    return render(
        request,
        'form.html',
        {
            'form': form,
        }
    )


def Form1_view(request):
    '''Renders a page with second function '''  # В разработке

    # if request.method == 'POST':
    #     os.chdir(BASE_DIR)
    #     form = InputFileForm(request.POST, request.FILES)
    #     files = request.FILES.getlist('file')
    #     if form.is_valid():
    #         dir_path, extract_type = handle_uploaded_file(files)   #places uploaded files in tmp dir
    #         cellcomm = form.cleaned_data['column_comment']+str(form.cleaned_data['row_comment'])
    #         cellvalue = form.cleaned_data['column_value']+str(form.cleaned_data['row_value'])
    #         result_file = form1Unit(dir_path, extract_type, cellcomm, cellvalue)   #opens each file, combines and save result file
    #
    #     return redirect('sendfile')
    #
    #
    # else:
    #     form = InputFileForm()
    return render(
        request,
        'form1.html',
        {
            # 'form': form,
        }
    )


def Form2_view(request):
    '''Renders a page with third function '''  # В разработке

    # if request.method == 'POST':
    #     os.chdir(BASE_DIR)
    #     form = InputFileForm(request.POST, request.FILES)
    #     files = request.FILES.getlist('file')
    #     if form.is_valid():
    #         dir_path, extract_type = handle_uploaded_file(files)   #places uploaded files in tmp dir
    #         cellcomm = form.cleaned_data['column_comment']+str(form.cleaned_data['row_comment'])
    #         cellvalue = form.cleaned_data['column_value']+str(form.cleaned_data['row_value'])
    #         result_file = form1Unit(dir_path, extract_type, cellcomm, cellvalue)   #opens each file, combines and save result file
    #
    #     return redirect('sendfile')
    #
    #
    # else:
    #     form = InputFileForm()
    return render(
        request,
        'form2.html',
        {
            # 'form': form,
        }
    )


def Form3_view(request):
    '''Renders a page with fourth function '''  # В разработке

    # if request.method == 'POST':
    #     os.chdir(BASE_DIR)
    #     form = InputFileForm(request.POST, request.FILES)
    #     files = request.FILES.getlist('file')
    #     if form.is_valid():
    #         dir_path, extract_type = handle_uploaded_file(files)   #places uploaded files in tmp dir
    #         cellcomm = form.cleaned_data['column_comment']+str(form.cleaned_data['row_comment'])
    #         cellvalue = form.cleaned_data['column_value']+str(form.cleaned_data['row_value'])
    #         result_file = form1Unit(dir_path, extract_type, cellcomm, cellvalue)   #opens each file, combines and save result file
    #
    #     return redirect('sendfile')
    #
    #
    # else:
    #     form = InputFileForm()
    return render(
        request,
        'form3.html',
        {
            # 'form': form,
        }
    )


def getResultFilesFromDisk(response):
    """returns result file to user and runs delayed subprocess to delete all files and dirs"""
    fp = FileResponse(open('result.xlsx', 'rb'), as_attachment=True, filename='result.xlsx')
    # print('до отравки в делит'+str(datetime.now()))
    # del_proc = Thread(target=deletefile())
    # del_proc.start()
    # return_proc = Thread(target= return fp)
    return fp


def getExampleFiles(response, form_num):
    """returns example files in form instructions"""

    fp = FileResponse(open('MEX3app/static/app/content/rogaikopyta' + str(form_num) + '.zip', 'rb'), as_attachment=True)
    return fp
