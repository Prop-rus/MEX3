import time
import zipfile
from datetime import datetime
from time import sleep

from openpyxl import load_workbook, Workbook
from django.http import FileResponse
from MEX3.settings import MEDIA_ROOT
import random
import os


def getFileExt(filename):
    ''' checking file format'''  # TODO its better to rewrite in re
    if filename.find('.zip') != -1:
        return '.zip'
    elif filename.find('.rar') != -1:
        return '.rar'
    elif filename.find('.7z') != -1:
        return '.7z'
    elif filename.find('.xls') != -1:
        return '.xls'
    elif filename.find('.xlsx') != -1:
        return '.xlsx'
    else:
        return 'wrong format'


def handle_uploaded_file(files):
    ''' Creates new tmp dir and uploads files there, returning dir path and file extension'''
    pat = 'MEX3app/filestoobr/'
    os.chdir(pat)
    name_dir = str(random.randint(1, 1000)) + (str(datetime.now())).replace(' ', '').replace('.', '').replace(':', '')
    new_dir = pat + name_dir
    os.mkdir(path=name_dir)
    os.chdir(name_dir)
    quantfiles = len(files)
    extract_type = ''
    if quantfiles == 1:
        ext = getFileExt(str(files[0]))
        if ext == 'wrong format':
            print('Сообщение о неверном формте')
            # TODO СОобщение о неверном формате
        elif ext == '.zip' or ext == '.rar' or ext == '.7z':
            extract_type = 'archive'
        else:
            extract_type = 'xlfiles'
    else:
        extract_type = 'xlfiles'
    for f in files:
        nfile = str(f)
        ext = getFileExt(nfile)
        if quantfiles > 1 and ext != '.xls' and ext != '.xlsx':
            print('Сообщение о неверном формте')
            # TODO Сообщение о неверном формате
        with open(nfile, 'wb+') as dest:
            for chunk in f.chunks():
                dest.write(chunk)
    # print(new_dir, extract_type)

    return new_dir, extract_type

    # TODO функция объединения


def form1Unit(dir_path, extract_type, cellcomm, cellvalue):
    '''Combines uploaded files in one dict, then writes it in result file'''

    if extract_type == 'archive':
        arch = zipfile.ZipFile(os.listdir()[0], 'r')
        filelist = arch.namelist()
    else:
        filelist = os.listdir()
    res_wb = Workbook()
    res_wsht = res_wb.active
    res_wsht.title = 'Лист с результатами'
    for file in filelist:
        if extract_type == 'archive':
            inner_file = zipfile.ZipFile.open(arch, file)

            wrkbook = load_workbook(inner_file, read_only=True)
        else:
            wrkbook = load_workbook(file, read_only=True)
        wrksheet = wrkbook.active
        # print(wrksheet.cell(column=int(cellcomm[0]), row=int(cellcomm[1])).value)
        comment = wrksheet.cell(column=int(cellcomm[0]), row=int(cellcomm[1])).value
        value = wrksheet.cell(column=int(cellvalue[0]), row=int(cellvalue[1])).value
        list_to_add = []
        list_to_add.append(file)
        list_to_add.append(comment)
        list_to_add.append(value)
        res_wsht.append(list_to_add)
        wrkbook.close()
    res_wb.save('result.xlsx')
    res_wb.close()
    return res_wb


def deletefile():
    '''deletes uploaded and result files after 1 min delay'''  # нужно переделать на celery..
    sleep(60)
    print('Пошло в делит' + str(datetime.now()))
    for file in os.listdir():
        os.remove(file)
    # os.chdir('..')
    # os.rmdir(name_dir)
