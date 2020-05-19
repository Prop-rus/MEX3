from django import forms
from .dicts import res, res_row
from .models import models


class InputFileForm(forms.Form):
    '''form for function that unites a set of files to one registry'''

    file = forms.FileField(label='Загрузите свои файлы', error_messages={'missing': "Файлы не выбраны"}, widget=forms.FileInput(attrs={'multiple': True}))
    column_comment = forms.ChoiceField(label="Выберите столбец \n", choices=res, widget=forms.Select(), initial=1)  # column for title
    row_comment = forms.ChoiceField(label="Выберите строку \n", choices=res_row, widget=forms.Select(), initial=1)  # row for title
    column_value = forms.ChoiceField(label="Выберите столбец \n", choices=res, widget=forms.Select(), initial=1)  # column for values
    row_value = forms.ChoiceField(label="Выберите строку \n", choices=res_row, widget=forms.Select(), initial=1)  # row for values


class InputFileForm1(forms.Form):
    '''form for funcion that devides one registry to different files'''

    file_to_fill = forms.FileField(label='Загрузите шаблон, для последующего заполнения данных из реестра', error_messages={'missing': "Файлы не выбраны"},
                                   widget=forms.FileInput(attrs={'multiple': False}))
    file = forms.FileField(label='Загрузите реестр для разбиеня на файлы', error_messages={'missing': "Файлы не выбраны"},
                           widget=forms.FileInput(attrs={'multiple': False}))
    column_comment_reg = forms.ChoiceField(label="Выберите столбец с подписями  \n", choices=res, widget=forms.Select(), initial=1)
    column_value_reg = forms.ChoiceField(label="Выберите столбец со значениями \n", choices=res, widget=forms.Select(), initial=1)
    column_comment_tofill = forms.ChoiceField(label="Столбец  \n", choices=res, widget=forms.Select(), initial=1)
    row_comment_tofill = forms.ChoiceField(label="Строка \n", choices=res_row, widget=forms.Select(), initial=1)
    column_value_tofill = forms.ChoiceField(label="Столбец \n", choices=res, widget=forms.Select(), initial=1)
    row_value_tofill = forms.ChoiceField(label="Строка \n", choices=res_row, widget=forms.Select(), initial=1)


class InputFileForm2(forms.Form):
    '''form for funcion that combines different regisries in on (in vertical loop  function way)'''

    file = forms.FileField(label='Загрузите реестры для объединения', error_messages={'missing': "Файлы не выбраны"}, widget=forms.FileInput(attrs={'multiple': True}))
    column_comment_reg = forms.ChoiceField(label="Выберите столбец с подписями  \n", choices=res, widget=forms.Select(), initial=1)
    column_value_reg = forms.ChoiceField(label="Выберите столбец со значениями \n", choices=res, widget=forms.Select(), initial=1)
