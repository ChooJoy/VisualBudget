# -*- coding: utf-8 -*-
import xlrd 
from django.conf import settings
from budgetelem.models import Document
import sys
import unicodedata

sys.setrecursionlimit(200)


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
        if amount == "": amount = 0
        try:
            amount = unicodedata.normalize('NFKD', amount).encode('ascii','ignore')
            amount = amount.replace(" ", "").replace(",", ".")
        except:
            pass
        if amount == "":
            amount = 0
        else:
            amount = float(amount)*unit_koef
            

        list_temp = {'name': name, 'amount': amount, 'deep': '-', 'id':'id0', 'parent': ''}                    
        list_elems.append(list_temp)         

        id_count = 1
        for rx in range(int(excel_name.start_budget)-1, int(excel_name.finish_budget)):

            name = sh.cell_value(rx, int(excel_name.name_column)-1)
            amount = sh.cell_value(rx, int(excel_name.amount_column)-1)
            if amount == "": amount = 0
        
            try:                
                amount = unicodedata.normalize('NFKD', amount).encode('ascii','ignore')
                amount = amount.replace(" ", "").replace(",", ".")
            except:
                pass                
            amount = float(amount)*unit_koef

            if sh.cell_value(rx, int(excel_name.amount_column)-1) != "" and amount != 0:                
                list_temp = {'name': name, 'amount': amount, 'deep': '-', 'id':'id'+str(id_count), 'parent': ''}                    
                list_elems.append(list_temp)   
                id_count += 1     


        basic_list = list_elems

        for elem in list_elems:
            elem['deep'] = '1'  

        flag_of_end, basic_list = make_deep(list_elems)

#        print flag_of_end

        json_obj = make_json(basic_list)
        
        csv_budget = make_csv(basic_list)

        excel_name.csv_obj = csv_budget
        excel_name.save()

        return flag_of_end, json_obj


def make_csv(csv_budget):

    csv_budget_string = ""
    for elem in csv_budget:
        csv_budget_string += elem['id'] + "," + elem['parent'] + ",\"" + elem['name'] + "\"," + str(elem['amount']) + "\n"


    return csv_budget_string


def make_json(list_elems):

    json_budget = ""
    
    global csv_budget
    csv_budget = list_elems

    json_budget = make_json_element(list_elems, 'id0', json_budget)

    return json_budget
                    
def make_json_element(list_elems, id_elem, json_budget):

    for elem in list_elems:
        flag = 0
        if elem['id'] == id_elem and elem['amount'] != 0:
            json_budget = json_budget + '{ \"label\":\"'+ elem['name'].replace('"', '\'').replace("\n", " ") + '\", \"amount\":\"' + str(elem['amount']) + '\"'      
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


def count_elems(children_list):

    count_elems_var = 0

    for elem in children_list:
        if elem['deep'] == '1':
            count_elems_var += 1            
    
    return count_elems_var - 1


#def print_without_children(children_list):
#    for elem in children_list:
#        if elem['deep'] == '1':
#            print elem['id'], elem['parent'], elem['name'], elem['amount']  
#    raw_input()

def make_deep(children_list):    

    stop_loop = 0


    list_elems = children_list 
    list_id = []
    count_elem = len(list_elems) - 1

    while len(list_elems) > 1 and stop_loop < 10000:
        
        children_list = find_children(list_elems, children_list, count_elem)        

        second_list = []
        

        for elem1 in children_list:
            if elem1['deep'] != '2':
                second_list_element = {'name': elem1['name'], 'amount': elem1['amount'], 'deep': '1', 'id': elem1['id'], 'parent': elem1['parent']}                    
                second_list.append(second_list_element)


        if list_elems == second_list:
            if count_elem > 0:
                count_elem -= 1
            else:
                count_elem = len(second_list) - 1                
        else:
            count_elem = len(second_list) - 1

        list_elems = second_list


        stop_loop += 1


    if stop_loop == 10000:
        return 1, children_list
    else:
        return 0, children_list


def find_children(list_elems, children_list, count_elem):

    list_id = []
    summ = round(list_elems[count_elem]['amount'], 2)
    list_id.append(list_elems[count_elem]['id'])

    while count_elem > 0:
        if round(list_elems[count_elem - 1]['amount'], 2) == round(summ, 2):
            children_list = make_parent_for_children(children_list, list_id, list_elems[count_elem - 1]['id'])
            break
        else:
            summ += round(list_elems[count_elem - 1]['amount'],2)
            list_id.append(list_elems[count_elem-1]['id'])
            count_elem -= 1
                
    return children_list

def make_parent_for_children(children_list, list_of_id, parent_id):

    for elem in list_of_id:

        for elem1 in children_list:
            if elem1['id'] == elem:
                elem1['deep'] = '2'
                elem1['parent'] = parent_id

    return children_list
        

