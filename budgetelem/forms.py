# -*- coding: utf-8 -*-
from django import forms
from budgetelem.models import Region    
from django.forms.extras.widgets import SelectDateWidget

class DocumentForm(forms.Form):

    docfile = forms.FileField(
        label='Выберите Excel-файл',
        widget=forms.ClearableFileInput(attrs={'class':'form-control', 'id': 'file', 'type':'button'}),
        error_messages={'required': 'Поле обязательно для заполнения'}
    )

    IN_OUT = (('1', 'Доходы',), ('2', 'Расходы',))

    PLAN_FACT = (('1', 'План',), ('2', 'Факт',), ('3', 'Уточнение',))

    FED_REGION_LOCAL = (('1', 'Федеральный уровень',),('2', 'Региональный уровень',),('3', 'Мунициальный уровень',))

    YEAR = (('1', '2016',),('2', '2015',),('3', '2014',),('4', '2013',),('5', '2012',),('6', '2011',),('7', '2010',),('8', '2009',),('9', '2008',),('10', '2007',),('11', '2006',),('12', '2005',),('13', '2004',),('14', '2003',),('15', '2002',),('16', '2001',),('17', '2000',))

    YEARS = {2000:('2000'),2001:('2001'),2002:('2002'),2003:('2003'),2004:('2004'),2005:('2005'),2006:('2006'),2007:('2007'),2008:('2008'),2009:('2009'),2010:('2010'),2011:('2011'),2012:('2012'),2013:('2013'),2014:('2014'),2015:('2015')}


    UNIT = (('1', 'руб.',),('2', 'тыс.руб.',), ('3', 'млн.руб.',))
 
    in_out = forms.ChoiceField(label='Доходы/расходы бюджета', choices=IN_OUT, widget=forms.Select(attrs={'class':'form-control', 'id':'select'}), error_messages={'required': 'Поле обязательно для заполнения'})    
    plan_fact = forms.ChoiceField(label='Планируемое/фактическое исполнение', choices=PLAN_FACT, widget=forms.Select(attrs={'class':'form-control', 'id':'plan_fact'}), error_messages={'required': 'Поле обязательно для заполнения'})
    data_budget = forms.DateField(label='Дата публикации бюджета', widget=SelectDateWidget(years = YEARS))
    fed_region_local = forms.ChoiceField(label='Уровень власти', choices=FED_REGION_LOCAL, error_messages={'required': 'Поле обязательно для заполнения'}, widget=forms.Select(attrs={'class':'form-control', 'id':'level'}))
    region = forms.ModelChoiceField(label='Регион', queryset=Region.objects.all(), required=False, widget=forms.Select(attrs={'class':'form-control', 'id':'region'}))
    local_name = forms.CharField(label='Наименование муниципалитета', max_length = 100, required=False, widget=forms.TextInput(attrs={'class':'form-control', 'id':'local_name', 'title':'Указывайте полное наименование, например: район Тропарево-Никулино, Село Степанчиково, город Владимир'}))
    authority_name = forms.CharField(label='Наименование органа власти', max_length = 500, error_messages={'required': 'Поле обязательно для заполнения'}, widget=forms.TextInput(attrs={'class':'form-control', 'id':'inputDefault', 'title':'По возможности заполняйте это поле официальным названием, например, "Правительство Воронежской области"'}))
    year = forms.ChoiceField(label='Год', choices=YEAR, error_messages={'required': 'Поле обязательно для заполнения'}, widget=forms.Select(attrs={'class':'form-control', 'id':'select'}))
    period = forms.IntegerField(label='Период', error_messages={'required': 'Поле обязательно для заполнения'}, widget=forms.TextInput(attrs={'class':'form-control', 'id':'inputDefault', 'title':'0 - весь год, иначе порядковый номер месяца окончания периода. (январь - 1, февраль - 2 и т.д.)'}))
    unit = forms.ChoiceField(label='Единица измерения', choices=UNIT, error_messages={'required': 'Поле обязательно для заполнения'}, widget=forms.Select(attrs={'class':'form-control', 'id':'select'}))
    source = forms.URLField(label='Источник бюджета', error_messages={'required': 'Поле обязательно для заполнения'}, widget=forms.TextInput(attrs={'class':'form-control', 'id':'inputDefault', 'title':'Ссылка либо на сам Excel-файл на сайте органа власти, либо на страницу, скоторой можно его скачать'}))
    sheet_number = forms.IntegerField(label='Номер страницы в Excel-файле', min_value=0, error_messages={'required': 'Поле обязательно для заполнения'}, widget=forms.TextInput(attrs={'class':'form-control', 'id':'sheet_num', 'title':'Порядковый номер страницы в Excel-файле'}))
    name_column = forms.IntegerField(label='Номер колонки с наименованием', min_value=0, error_messages={'required': 'Поле обязательно для заполнения'}, widget=forms.TextInput(attrs={'class':'form-control', 'id':'inputDefault', 'title':'Порядковый номер столбца, в котором расположены наименования показателей'}))
    amount_column = forms.IntegerField(label='Номер колонки с суммой', min_value=0, error_messages={'required': 'Поле обязательно для заполнения'}, widget=forms.TextInput(attrs={'class':'form-control', 'id':'inputDefault'}))
    sum_row = forms.IntegerField(label='Строка с общей суммой бюджета', min_value=0, error_messages={'required': 'Поле обязательно для заполнения'}, widget=forms.TextInput(attrs={'class':'form-control', 'id':'inputDefault', 'title':'Укажите СТРОКУ, а не столбец, где находится итоговая сумма. Обычно это "Итого/Всего расходов/Всего доходов" или название ведомства.'}))
    start_budget = forms.IntegerField(label='С какой строки начинается бюджет', min_value=0, error_messages={'required': 'Поле обязательно для заполнения'}, widget=forms.TextInput(attrs={'class':'form-control', 'id':'inputDefault', 'title':'Строка с которой начинается бюджет. Исключая строку общей суммы.'}))
    finish_budget = forms.IntegerField(label='На какой строке заканчивается бюджет', min_value=0, error_messages={'required': 'Поле обязательно для заполнения'}, widget=forms.TextInput(attrs={'class':'form-control', 'id':'inputDefault', 'title':'Строка, которой заканчивается бюджет. Исключая строку общей суммы.'}))
    description = forms.CharField(label='Описание, пояснение', widget=forms.Textarea(attrs={'class':'form-control', 'id':'textArea'}), required=False)
