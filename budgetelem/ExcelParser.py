import xlrd 
from django.conf import settings
from budgetelem.models import Document

class ExcelParser(object):
      

    def read_excel(self, excel_name):

        list_elems = []
        path = settings.MEDIA_ROOT+excel_name.docfile.name
        print path
        book = xlrd.open_workbook(path)
        print "The number of worksheets is", book.nsheets
        print "Worksheet name(s):", book.sheet_names()
        sh = book.sheet_by_index( int(excel_name.sheet_number)-1 )
        #print sh.name, sh.nrows, sh.ncols

        #print "Cell D30 is", sh.cell_value(rowx=29, colx=3)
        for rx in range(int(excel_name.start_budget)-1, int(excel_name.finish_budget)):
            name = sh.cell_value(rx, int(excel_name.name_column)-1)
            amount = sh.cell_value(rx, int(excel_name.amount_column)-1)
            list_temp = {'name': name, 'amount': amount, 'deep': '1'}                    
            list_elems.append(list_temp)        

        #for elem in list_elems:
        #    print elem['name'], elem['amount'], elem['deep']

        make_deep(list_elems)
        #print excel_name.in_out  
        #print excel_name.plan_fact 
        #print excel_name.sheet_number 
        #print excel_name.code_column  
        #print excel_name.name_column  
        #print excel_name.amount_column 
        #print excel_name.start_budget  
        #print excel_name.finish_budget

        return excel_name

def make_deep(list_elems):
    count_deep = 1
    count_elem = len(list_elems) - 1
    temp_amount = list_elems[len(list_elems)-1]['amount']
    
    while count_elem != 0: 
        if int(list_elems[count_elem]['deep']) == count_deep:
            #print list_elems[count_elem]['deep'], count_deep
            #print temp_amount, list_elems[count_elem-1]['amount']
            if temp_amount == list_elems[count_elem-1]['amount']:
                list_elems[count_elem-1]['deep'] = count_deep + 1
                temp_amount = list_elems[count_elem-2]['amount']
                count_elem -= 2
                if count_elem < 0:
                    break
            else: 
                temp_amount += list_elems[count_elem-1]['amount']
                count_elem -= 1        
 
    for elem in list_elems:
            print elem['name'], elem['amount'], elem['deep']

