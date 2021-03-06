# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from budgetelem.models import Region

class Command(BaseCommand):

    def handle(self, *args, **options):


        fin_list = []

        r = open('/home/choojoy/i-graph/orders/vrnbudget/budgetelem/management/commands/regions.txt', 'rb')
        r_lines = r.readlines()

        c = open('/home/choojoy/i-graph/orders/vrnbudget/budgetelem/management/commands/codes.txt', 'rb')
        c_lines = c.readlines()
        

        count_elem = 0
        while count_elem<11:
   
            split_list = r_lines[count_elem].split("\t")
            split_list2 = c_lines[count_elem].split("\t")
            #list_temp = { 'code_rus': split_list[0], 'square':split_list[4].replace(" ", ''), 'people':split_list[5].replace(" ", ''), 'capital':split_list[6], 'okato':split_list[8], 'date_people': 2010, 'name':split_list2[0], 'code_iso':split_list2[3] }
            new_region = Region(
                name = split_list2[0],
                code_rus = split_list[0],
                code_iso = split_list2[3], 
                code_okato = split_list[8],
                capital = split_list[6],
                square = split_list[4].replace(" ", ''),
                people = split_list[5].replace(" ", ''),
                date_people = '2010-01-01')
            new_region.save()
        
            count_elem += 1
