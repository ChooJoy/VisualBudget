# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Region.code_okato'
        db.add_column('budgetelem_region', 'code_okato',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Region.code_okato'
        db.delete_column('budgetelem_region', 'code_okato')


    models = {
        'budgetelem.belem': {
            'Meta': {'object_name': 'BElem'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'budgetelem.codesprofit': {
            'Meta': {'object_name': 'CodesProfit'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'deep': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        'budgetelem.document': {
            'Meta': {'object_name': 'Document'},
            'amount_column': ('django.db.models.fields.IntegerField', [], {}),
            'code_column': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'csv_obj': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'docfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'finish_budget': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_out': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'json_obj': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name_column': ('django.db.models.fields.IntegerField', [], {}),
            'plan_fact': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'sheet_number': ('django.db.models.fields.IntegerField', [], {}),
            'start_budget': ('django.db.models.fields.IntegerField', [], {}),
            'sum_row': ('django.db.models.fields.IntegerField', [], {})
        },
        'budgetelem.econokr': {
            'Meta': {'object_name': 'EconOkr'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'budgetelem.fedokr': {
            'Meta': {'object_name': 'FedOkr'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'budgetelem.region': {
            'Meta': {'object_name': 'Region'},
            'code_iso': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'code_okato': ('django.db.models.fields.IntegerField', [], {}),
            'code_rus': ('django.db.models.fields.IntegerField', [], {}),
            'date_people': ('django.db.models.fields.DateField', [], {}),
            'econokr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['budgetelem.EconOkr']"}),
            'end_year': ('django.db.models.fields.DateField', [], {}),
            'fedokr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['budgetelem.FedOkr']"}),
            'flag': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'people': ('django.db.models.fields.IntegerField', [], {}),
            'square': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['budgetelem']