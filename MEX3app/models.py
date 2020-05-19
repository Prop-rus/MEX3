from django.db import models

# Create your models here.
from .dicts import res


class tmp_dir_ready_status(models.Model):
    token = models.CharField('token', max_length=150)
    dir_name = models.CharField('Temp dir for loaded files', max_length=50)
    res_ready = models.BooleanField('Flag to resualt is ready', default=False)


class Type_of_edit(models.Model):
    name = models.CharField('Тип обработки', max_length=150)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип обработки'
        verbose_name_plural = 'Типы обработки'


class Column(models.Model):
    col = models.IntegerField(choices=res)
