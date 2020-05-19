import os
from django.http import request, HttpRequest, HttpResponseRedirect, HttpResponse, FileResponse
from django.shortcuts import render, redirect
from datetime import datetime
from .models import tmp_dir_ready_status
from MEX3.settings import MEDIA_ROOT, BASE_DIR
from .forms import InputFileForm, InputFileForm1, InputFileForm2
from .backend import handle_uploaded_file, form0Unit, form1Unit, form2Unit
from .tasks import deletefile


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
        token = request.COOKIES['csrftoken']
        form = InputFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('file')
        if form.is_valid():
            dir_path, name_dir, files, saved_obj, wrong_f = handle_uploaded_file(files, token=token)  # places uploaded files in tmp dir
            if wrong_f:
                return render(
                    request,
                    'wrong_format.html',
                )
            cellcomm = form.cleaned_data['column_comment'] + str(form.cleaned_data['row_comment'])
            cellvalue = form.cleaned_data['column_value'] + str(form.cleaned_data['row_value'])
            form0Unit(dir_path, cellcomm, cellvalue)  # opens each file, combines and saves result file
            saved_obj.res_ready = True  # this will be used by ajax as a sign to finish waiting visualization
            saved_obj.save()
            deletefile(dir_pat=dir_path)
            return redirect('sendfile', name_dir)

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
    '''Renders a page with second function '''

    if request.method == 'POST':
        token = request.COOKIES['csrftoken']
        form = InputFileForm1(request.POST, request.FILES)
        files_reg = request.FILES.getlist('file')
        files_tofill = request.FILES.getlist('file_to_fill')
        if form.is_valid():
            dir_path, name_dir, files_reg2, saved_obj, wrong_f = handle_uploaded_file(files_reg, token=token)  # places registry file in tmp dir
            if wrong_f:
                return render(
                    request,
                    'wrong_format.html',
                )
            dir_path_tofill, name_dir2, files_tofill2, saved_obj2, wrong_f = handle_uploaded_file(files_tofill, dirpath=dir_path,
                                                                                                  token=token)  # places template file in tmp dir
            if wrong_f:
                return render(
                    request,
                    'wrong_format.html',
                )
            reg_com = form.cleaned_data['column_comment_reg']
            reg_value = form.cleaned_data['column_value_reg']
            cell_comment_tofill = form.cleaned_data['column_comment_tofill'] + str(form.cleaned_data['row_comment_tofill'])
            cell_val_to_fill = form.cleaned_data['column_value_tofill'] + str(form.cleaned_data['row_value_tofill'])
            form1Unit(
                dir_path,
                files_reg2[0],
                files_tofill2[0],
                cell_comment_tofill,
                cell_val_to_fill,
                reg_com,
                reg_value
            )
            saved_obj.res_ready = True
            saved_obj.save()
            saved_obj2.res_ready = True
            saved_obj2.save()
            deletefile(dir_pat=dir_path)

            return redirect('sendfile', name_dir)

    else:
        form = InputFileForm1()
    return render(
        request,
        'form1.html',
        {
            'form': form,
        }
    )


def Form2_view(request):
    '''Renders a page with third function '''

    if request.method == 'POST':
        token = request.COOKIES['csrftoken']
        form = InputFileForm2(request.POST, request.FILES)
        files = request.FILES.getlist('file')
        if form.is_valid():
            dir_path, name_dir, files, saved_obj, wrong_f = handle_uploaded_file(files, token=token)  # places uploaded files in tmp dir
            if wrong_f:
                return render(
                    request,
                    'wrong_format.html',
                )
            reg_com = form.cleaned_data['column_comment_reg']
            reg_value = form.cleaned_data['column_value_reg']
            form2Unit(dir_path, reg_com, reg_value)  # opens each file, combines and save result file
            saved_obj.res_ready = True
            saved_obj.save()
            deletefile(dir_pat=dir_path)
            return redirect('sendfile', name_dir)

    else:
        form = InputFileForm2()
    return render(
        request,
        'form2.html',
        {
            'form': form,
        }
    )


def getResultFilesFromDisk(response, dir_path):
    """returns result file to user """

    path = os.path.join('MEX3app/filestoobr/' + dir_path + '/' + 'result/')
    fp = FileResponse(open(path + os.listdir(path)[0], 'rb'), as_attachment=True)
    return fp


def getExampleFiles(response, form_num):
    """returns example files in form instructions"""

    fp = FileResponse(open('MEX3app/static/app/content/rogaikopyta' + str(form_num) + '.zip', 'rb'), as_attachment=True)
    return fp


def test_ajax(request, num=''):
    '''ajax asks this view the result file is redy or not. This view looks its flag in db'''

    if request.method == 'GET':
        ready_obj = tmp_dir_ready_status.objects.filter(token=request.COOKIES['csrftoken']).exclude(res_ready=True).count()
        if ready_obj > 0:
            return HttpResponse('NOT', content_type='text/html')
        else:
            return HttpResponse('READY', content_type='text/html')
    else:
        return HttpResponse('BYE', content_type='text/html')
