# -*- coding: utf-8 -*-
import xlrd 
from django.conf import settings
from budgetelem.models import Document
import sys
import unicodedata

sys.setrecursionlimit(200)

basic_list = []
csv_budget = []


class ExcelParser(object):

    def read_excel(self, excel_name):


        if excel_name.unit == '1':
            unit_koef = 1
        elif excel_name.unit == '2':
            unit_koef = 1000
        elif excel_name.unit == '3':
            unit_koef = 1000000

        list_elems = []
        path = settings.MEDIA_ROOT+excel_name.docfile.name
        book = xlrd.open_workbook(path)
#        print "The number of worksheets is", book.nsheets
#        print "Worksheet name(s):", book.sheet_names()
        sh = book.sheet_by_index( int(excel_name.sheet_number)-1 )

        name = sh.cell_value(int(excel_name.sum_row)-1, int(excel_name.name_column)-1)
        
        amount = sh.cell_value(int(excel_name.sum_row)-1, int(excel_name.amount_column)-1)
        try:
            amount = unicodedata.normalize('NFKD', amount).encode('ascii','ignore')
            amount = amount.replace(" ", "").replace(",", ".")
        except:
            pass
        amount = float(amount)*unit_koef
        list_temp = {'name': name, 'amount': amount, 'deep': '-', 'id':'id0', 'parent': ''}                    
        list_elems.append(list_temp)         

        id_count = 1
        for rx in range(int(excel_name.start_budget)-1, int(excel_name.finish_budget)):
            if sh.cell_value(rx, int(excel_name.amount_column)-1) != "":            
                name = sh.cell_value(rx, int(excel_name.name_column)-1)
                amount = sh.cell_value(rx, int(excel_name.amount_column)-1)
                try:                
                    amount = unicodedata.normalize('NFKD', amount).encode('ascii','ignore')
                    amount = amount.replace(" ", "").replace(",", ".")
                except:
                    pass                
                amount = float(amount)*unit_koef    
                list_temp = {'name': name, 'amount': amount, 'deep': '-', 'id':'id'+str(id_count), 'parent': ''}                    
                list_elems.append(list_temp)   
                id_count += 1     

       

        global basic_list 
        basic_list = list_elems

        

        list_elems = make_deep(list_elems)

#        print list_elems

        json_obj = make_json(list_elems)
        
        global csv_budget
        csv_budget = make_csv(csv_budget)

        print csv_budget
        excel_name.csv_obj = csv_budget
        excel_name.save()

        return json_obj


def make_csv(csv_budget):

    csv_budget_string = ""
    for elem in csv_budget:
        csv_budget_string += elem['id'] + "," + elem['parent'] + ",\"" + elem['name'] + "\"," + str(elem['amount']) + "\n"


    return csv_budget_string

def make_deep(list_elems):    

    stop_loop = 0
    while len(list_elems)>1:
        
        count_elem = len(list_elems) -1
        current_deep = 1
        while count_elem >= 0:    
            count_elem = find_children(list_elems, count_elem, current_deep)
            break
    
        second_list = []    
        for elem in list_elems:
            if elem['deep'] != '2':
                second_list.append(elem)

        list_elems = second_list

        stop_loop += 1
        if stop_loop == 100:          
            break
        
    return list_elems    


def find_elem(list_elems, id_elem, parent_id):
    
    element = [elem for elem in list_elems if elem['id'] == id_elem]
    element[0]['parent'] = parent_id


def find_children(list_elems, temp_count_elem, current_deep):
    
    temp_count_elem_for_return = temp_count_elem
    summ = round(list_elems[temp_count_elem]['amount'],2)
    num_child = 0
    while temp_count_elem > 0 :
        if round(list_elems[temp_count_elem-1]['amount'], 2) == round(summ, 2):
            list_elems[temp_count_elem-1]['deep'] = 1
            while num_child >= 0:
                list_elems[temp_count_elem+num_child]['deep'] = 2
                print list_elems[temp_count_elem+num_child]['id'], list_elems[temp_count_elem-1]['id']
                find_elem(list_elems, list_elems[temp_count_elem+num_child]['id'], list_elems[temp_count_elem-1]['id'])
                num_child -= 1
            return temp_count_elem - 1
            
        else: 
            summ += round(list_elems[temp_count_elem-1]['amount'], 2)
            num_child += 1
            temp_count_elem -= 1

    return temp_count_elem_for_return - 1

def make_json(list_elems):

    json_budget = ""
    
    global csv_budget
    csv_budget = list_elems

    json_budget = make_json_element(list_elems, 'id0', json_budget)

    return json_budget
                    
def make_json_element(list_elems, id_elem, json_budget):

    for elem in list_elems:
        flag = 0
        if elem['id'] == id_elem:
            json_budget = json_budget + '{ \"label\":\"'+ elem['name'].replace('"', '\'') + '\", \"amount\":\"' + str(elem['amount']) + '\"'      
            for elem2 in list_elems:
                if elem2['parent'] == id_elem:
                    json_budget = json_budget + ',\"children\": ['
                    break            

            for elem2 in list_elems:
                if elem2['parent'] == id_elem:
                    flag = 1
                    json_budget = make_json_element(list_elems, elem2['id'], json_budget)
                    json_budget = json_budget + ']'
            json_budget = json_budget + '}'

    json_budget = json_budget.replace('}]{', '},{')

    return json_budget
