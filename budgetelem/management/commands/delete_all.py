# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from budgetelem.models import Region, FedOkr, EconOkr

class Command(BaseCommand):

    def handle(self, *args, **options):

        econ_okr_val = "Северо-Кавказский " + "экономический район"

        econ_okr = EconOkr.objects.get(name = econ_okr_val)
        print econ_okr.name
        print '--------------------------------------------------'

        r = open('/home/choojoy/i-graph/orders/vrnbudget/docs/tempdoc', 'rb')
        r_lines = r.readlines()

        for line in r_lines:
            r = Region.objects.get(name = line.strip())
            print r.name
            r.econokr = econ_okr
            r.save()
        
