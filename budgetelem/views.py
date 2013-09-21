# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.servers.basehttp import FileWrapper

from budgetelem.models import Document
from budgetelem.models import Region
from budgetelem.forms import DocumentForm
from budgetelem.ExcelParserBig import ExcelParser

import json
import csv
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings


def index(request):
    # Load documents for the list page
    documents = Document.objects.all()
    num_docs = len(documents)
    fed_docs = Document.objects.filter(fed_region_local = "1")
    reg_docs = Document.objects.filter(fed_region_local = "2")
    loc_docs = Document.objects.filter(fed_region_local = "3")

    num_fed_docs =  len(fed_docs)
    num_reg_docs =  len(reg_docs)
    num_loc_docs = len(loc_docs)

    regions = Region.objects.all()

    region_data_to_js = []    

    for elem in regions:
        num_reg_doc = len(Document.objects.filter(region = elem ).filter(fed_region_local = '2'))
        num_loc_doc = len(Document.objects.filter(region = elem ).filter(fed_region_local = '3'))
        region_data_to_js.append({'code_iso': elem.code_iso, 'flag': elem.flag, 'capital': elem.capital, 'code_rus': elem.code_rus, 'fedokr': elem.fedokr.name, 'econokr': elem.econokr.name, 'square': elem.square, 'people': elem.people, 'num_loc_doc': num_loc_doc, 'num_reg_doc': num_reg_doc,})

    region_data_to_js = json.dumps(region_data_to_js)


    # Render list page with the documents and the form
    return render_to_response(
        'budget/index.html',
        {'documents': documents, 'region_data': region_data_to_js, 'num_fed_docs': num_fed_docs, 'num_reg_docs': num_reg_docs, 'num_loc_docs': num_loc_docs, 'num_docs': num_docs,  'fed_docs': fed_docs[0:10], 'reg_docs': reg_docs[0:10], 'loc_docs': loc_docs[0:10] })

def all_budgets(request):
    documents = Document.objects.all()
    fed_region_local = "Все бюджеты"
    type_budget = 0

    return render_to_response(
        'budget/budgets.html',
        {'documents': documents, 'fed_region_local': fed_region_local, 'type_budget': type_budget})


def federal(request):
    documents = Document.objects.filter(fed_region_local = '1')
    fed_region_local = "Федеральные бюджеты"
    type_budget = 1

    return render_to_response(
        'budget/budgets.html',
        {'documents': documents, 'fed_region_local': fed_region_local, 'type_budget': type_budget})

def regional(request):
    documents = Document.objects.filter(fed_region_local = '2')
    fed_region_local = "Региональные бюджеты"
    type_budget = 2

    return render_to_response(
        'budget/budgets.html',
        {'documents': documents, 'fed_region_local': fed_region_local, 'type_budget': type_budget})

def local(request):
    documents = Document.objects.filter(fed_region_local = '3')
    fed_region_local = "Местные бюджеты"
    type_budget = 3

    return render_to_response(
        'budget/budgets.html',
        {'documents': documents, 'fed_region_local': fed_region_local, 'type_budget': type_budget})



def region(request, region_code):

    documents = Document.objects.filter(region__code_rus = region_code)
    region = Region.objects.get(code_rus = region_code)
    num_reg = len(Document.objects.filter(region__code_rus = region_code).filter(fed_region_local = '2'))
    num_loc = len(Document.objects.filter(region__code_rus = region_code).filter(fed_region_local = '3'))

    return render_to_response(
        'budget/region.html',
        {'documents': documents, 'region': region, 'num_reg':num_reg, 'num_loc':num_loc,})


def budget(request, budget_id):

    doc = get_object_or_404(Document, pk = budget_id)
    if doc.region:
        region = Region.objects.get(name = doc.region.name)
    else:
        region = 0

    json_obj = doc.json_obj

    return render_to_response(
        'budget/budget.html',
        {'region': region, 'doc': doc, 'json_obj': json_obj})


def add(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():           

            newdoc = Document(
                docfile = request.FILES['docfile'], 
                in_out = request.POST['in_out'], 
                plan_fact = request.POST['plan_fact'], 
                data_budget = request.POST['data_budget_year']+'-'+request.POST['data_budget_month']+ '-' +request.POST['data_budget_day'],
                fed_region_local = request.POST['fed_region_local'], 
                local_name = request.POST['local_name'],
                authority_name = request.POST['authority_name'],
                year = request.POST['year'],
                period = request.POST['period'],
                unit = request.POST['unit'],
                source = request.POST['source'],
                description = request.POST['description'],
                sheet_number = request.POST['sheet_number'], 
                name_column = request.POST['name_column'], 
                amount_column = request.POST['amount_column'],
                sum_row = request.POST['sum_row'], 
                start_budget = request.POST['start_budget'], 
                finish_budget = request.POST['finish_budget'])           
            newdoc.save()

#            print newdoc.data_budget
            
            excel_parser = ExcelParser()
            temp_region = 0
            flag_of_end, json_obj = excel_parser.read_excel(newdoc)
                
            if flag_of_end == 0:
                newdoc.json_obj = json_obj
                if request.POST['region'] != "":
                    temp_region = int(request.POST['region'])
                    temp_region = Region.objects.get(id = temp_region) 
                    newdoc.region = temp_region
                else: 
                    temp_region = 0
                newdoc.save()            
                return render_to_response('budget/budget.html', {'region': temp_region, 'doc': newdoc, 'json_obj': json_obj})
            elif flag_of_end == 1:
                newdoc.delete()                    
                return render_to_response('static/error.html')            
    else:
        form = DocumentForm() # A empty, unbound form

    
    return render_to_response(
        'budget/add.html',
        {'form': form},
        context_instance=RequestContext(request)
    )

def table(request, document_id):

    p = get_object_or_404(Document, pk=document_id)
    json_obj = p.json_obj    

    return render_to_response('budget/table.html', {'document': p, 'json_obj': json_obj})


def view_one(request, document_id):

    p = get_object_or_404(Document, pk=document_id)
    if p.region:
        region = Region.objects.get(name = p.region.name)
    else:
        region = 0
    json_obj = p.json_obj    

    return render_to_response('budget/bubbletree.html', {'doc': p, 'json_obj': json_obj, 'region':region})

def view_two(request, document_id):

    p = get_object_or_404(Document, pk=document_id)
    if p.region:
        region = Region.objects.get(name = p.region.name)
    else:
        region = 0
    json_obj = p.json_obj
    json_obj = json_obj.replace('label', 'name')
    json_obj = json_obj.replace(', \"amount\"', ',\"color\": \"#119ce2\", \"cx\": \"\", \"cy\": \"\", \"width\": \"\", \"height\": \"\", \"amount\"')    

    return render_to_response('budget/treemap.html', {'doc': p, 'json_obj': json_obj, 'region':region})

def generate_csv(request, document_id):

    filename = document_id + '.csv'
    
#    print document_id
    p = get_object_or_404(Document, pk=document_id)   
#    print p.csv_obj
 
    response = HttpResponse(p.csv_obj, content_type="text/plain")
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response

def generate_json(request, document_id):

    filename = document_id + '.json'
    
    p = get_object_or_404(Document, pk=document_id)   
 
    response = HttpResponse(p.json_obj, content_type="text/plain")
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response
