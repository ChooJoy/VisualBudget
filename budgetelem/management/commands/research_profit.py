# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from budgetelem.models import CodesProfit
import pickle

class Command(BaseCommand):
    args = '<path path ...>'
    help = 'Модуль разбора бюджетных доходов'

    def handle(self, *args, **options):

        w = open('/home/choojoy/i-graph/orders/vrnbudget/files/profit_codes.json', 'wb')

        for path in args:
            f=open(path, 'rb')
            lines = f.readlines()
            flag = 0
            list_profit = []

            for line in lines:
                #print len(line) 
                #print line.decode('utf-8')
                code_temp = line[:34].replace(' ', '')[:20]

                if len(code_temp) == 20:  
                    
                    if flag == 1:
                        list_temp = {'code': code, 'name': name, 'deep': deep}                    
                        list_profit.append(list_temp)
                    flag = 1

                    code = code_temp                  
                    #print code
                    deep = line[len(line)-2:len(line)-1]
                    #print deep
                    name = line[32:len(line)-3].strip()
                elif len(code_temp) == 1:
                    name = name + ' ' + line[32:len(line)-1].strip()
                else: 
                    print 'wtf'
                    break
                
        len_name = 0
        for elem in list_profit:
            elem['name'] = ' '.join(elem['name'].split())
            #if len(elem['name']) > len_name: len_name = len(elem['name'])                
            #print len_name

        for elem in list_profit:
            w.write('{"code":"' + elem['code'] + '","name":"' + elem['name'] + '":"deep":"' + elem['deep'] + '"},')
        
        print len(list_profit)

        f.close
        #w.close
        
        count = 0
        for elem in list_profit:
            if elem['deep'] == '\x83': elem['deep']=10
            code_add = CodesProfit(code = elem['code'], name = elem['name'], deep = int(elem['deep']))
            code_add.save()
            count += 1
            print count
