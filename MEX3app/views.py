import mimetypes
import os

from django.http import request, HttpRequest, HttpResponseRedirect, HttpResponse, FileResponse
from django.shortcuts import render, redirect
from datetime import datetime
from .forms import InputFileForm


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
    '''Renders a form page to upload file'''
    filestodownl =  os.listdir('MEX3app/media/')
    if request.method == 'POST':
        form = InputFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('file')
        if form.is_valid():
            for n, afile in enumerate(files):
                # handle_uploaded_file(afile,n)
                pass
        return redirect('sendfile')


    else:
        form = InputFileForm()
    return render(
        request,
        'form.html',
        {
            'form': form,
            'files': filestodownl,
        }
    )

# def handle_uploaded_file(f,n):
#     with open(f'MEX3app/media/data{n}.xlsx', 'wb+') as dest:
#         for chunk in f.chunks():
#             dest.write(chunk)

def getFilesFromDisk(response):
    pat ='MEX3app/media/'
    file = 'MEX3app/media/testfile.xlsx'
    fp = FileResponse(open(file,'rb'), as_attachment=True, filename='result.xlsx')

    return fp

