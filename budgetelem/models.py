# -*- coding: utf-8 -*-

from django.db import models
from django import forms

class BElem(models.Model):
    name = models.CharField(max_length = 200)
    amount = models.IntegerField()


class CodesProfit(models.Model):
    code = models.CharField(max_length = 20)
    name = models.TextField()
    deep = models.IntegerField()

class FedOkr(models.Model):
    name = models.CharField(max_length = 100)
    center = models.CharField(max_length = 30)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Федеральные округа'
        verbose_name_plural = 'Федеральные округа'


class EconOkr(models.Model):
    name = models.CharField(max_length = 100)
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Экономические округа'
        verbose_name_plural = 'Экономические округа'

class Region(models.Model):
    name = models.CharField('Название', max_length = 100)
    end_year = models.DateField('Год окончания существования',blank=True)
    code_rus = models.IntegerField('Код региона')
    code_iso = models.CharField('Код региона по ISO',max_length = 6)
    code_okato = models.IntegerField('Код региона по ОКАТО')
    capital = models.CharField ('Столица', max_length = 30)
    capital_coords_lat = models.CharField(max_length = 11)     
    capital_coords_lng = models.CharField(max_length = 11)
    flag = models.CharField ('Название файла с флагом', max_length = 12, null=True)
    fedokr = models.ForeignKey(FedOkr, verbose_name='Федеральный округ', null=True)
    econokr = models.ForeignKey(EconOkr, verbose_name='Экономический округ', null=True)
    square = models.IntegerField('Территорим, км2')
    people = models.IntegerField('Население')
    date_people = models.DateField('Дата(наседение)')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Регионы РФ'
        verbose_name_plural = 'Регионы РФ'

class Document(models.Model):

    IN_OUT = (('1', 'Доходы',), ('2', 'Расходы',))
    PLAN_FACT = (('1', 'План',), ('2', 'Факт',), ('3', 'Уточнение',))
    FED_REGION_LOCAL = (('1', 'Федеральный уровень',),('2', 'Региональный уровень',),('3', 'Мунициальный уровень',))

    YEAR = (('1', '2016',),('2', '2015',),('3', '2014',),('4', '2013',),('5', '2012',),('6', '2011',),('7', '2010',),('8', '2009',),('9', '2008',),('10', '2007',),('11', '2006',),('12', '2005',),('13', '2004',),('14', '2003',),('15', '2002',),('16', '2001',),('17', '2000',))

    UNIT = (('1', 'руб.',),('2', 'тыс.руб.',), ('3', 'млн.руб.',))

    docfile = models.FileField(upload_to='documents')
    in_out = models.CharField(max_length = 1, choices=IN_OUT)    
    plan_fact = models.CharField(max_length = 1, choices=PLAN_FACT)
    fed_region_local = models.CharField(max_length = 1, choices=FED_REGION_LOCAL)
    region = models.ForeignKey(Region, blank=True, null=True)
    local_name = models.CharField(max_length = 100, blank=True)
    local_coords_lat = models.CharField(max_length = 11)     
    local_coords_lng = models.CharField(max_length = 11)
    authority_name = models.CharField(max_length = 500)
    year = models.CharField(max_length = 2, choices=YEAR)
    period = models.IntegerField()
    data_budget = models.DateField('Дата публикации бюджета', blank=True, null=True)
    unit = models.CharField(max_length = 2, choices=UNIT)
    source = models.URLField()
    sheet_number = models.IntegerField()
    name_column = models.IntegerField()
    amount_column = models.IntegerField()
    sum_row = models.IntegerField()
    start_budget = models.IntegerField()
    finish_budget = models.IntegerField()
    description = models.TextField(blank=True)
    json_obj = models.TextField(blank=True)
    csv_obj = models.TextField(blank=True)

    def __unicode__(self):
        return self.authority_name

    class Meta:
        verbose_name = 'Документы'
        verbose_name_plural = 'Документы'




