from django import forms
from .dicts import res, res_row
from .models import models

class InputFileForm(forms.Form):
    file = forms.FileField(label='Загрузите свои файлы', error_messages={'missing': "Файлы не выбраны"}, widget=forms.FileInput(attrs={'multiple':True}))
    column_comment = forms.ChoiceField(label="Выберите столбец \n", choices = res, widget=forms.Select(), initial=1)
    row_comment = forms.ChoiceField(label="Выберите строку \n", choices = res_row, widget=forms.Select(), initial=1)
    column_value = forms.ChoiceField(label="Выберите столбец \n", choices = res, widget=forms.Select(), initial=1)
    row_value = forms.ChoiceField(label="Выберите строку \n", choices = res_row, widget=forms.Select(), initial=1)

#TODO сделать опцию выбора подписей к строкам - по названию файла или по ячейке

