from django import forms


class InputFileForm(forms.Form):
    file = forms.FileField(label='Загрузите свои файлы', error_messages={'missing': "Файлы не выбраны"}, widget=forms.FileInput(attrs={'multiple':True}))
