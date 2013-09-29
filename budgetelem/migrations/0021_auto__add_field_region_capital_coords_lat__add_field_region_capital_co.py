# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Region.capital_coords_lat'
        db.add_column('budgetelem_region', 'capital_coords_lat',
                      self.gf('django.db.models.fields.CharField')(default=0.0, max_length=10),
                      keep_default=False)

        # Adding field 'Region.capital_coords_lng'
        db.add_column('budgetelem_region', 'capital_coords_lng',
                      self.gf('django.db.models.fields.CharField')(default=0.0, max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Region.capital_coords_lat'
        db.delete_column('budgetelem_region', 'capital_coords_lat')

        # Deleting field 'Region.capital_coords_lng'
        db.delete_column('budgetelem_region', 'capital_coords_lng')


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
            'authority_name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'csv_obj': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'data_budget': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'docfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'fed_region_local': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'finish_budget': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_out': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'json_obj': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'local_coords_lat': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'local_coords_lng': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'local_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name_column': ('django.db.models.fields.IntegerField', [], {}),
            'period': ('django.db.models.fields.IntegerField', [], {}),
            'plan_fact': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['budgetelem.Region']", 'null': 'True', 'blank': 'True'}),
            'sheet_number': ('django.db.models.fields.IntegerField', [], {}),
            'source': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'start_budget': ('django.db.models.fields.IntegerField', [], {}),
            'sum_row': ('django.db.models.fields.IntegerField', [], {}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'budgetelem.econokr': {
            'Meta': {'object_name': 'EconOkr'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'budgetelem.fedokr': {
            'Meta': {'object_name': 'FedOkr'},
            'center': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'budgetelem.region': {
            'Meta': {'object_name': 'Region'},
            'capital': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'capital_coords_lat': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'capital_coords_lng': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'code_iso': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'code_okato': ('django.db.models.fields.IntegerField', [], {}),
            'code_rus': ('django.db.models.fields.IntegerField', [], {}),
            'date_people': ('django.db.models.fields.DateField', [], {}),
            'econokr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['budgetelem.EconOkr']", 'null': 'True'}),
            'end_year': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'fedokr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['budgetelem.FedOkr']", 'null': 'True'}),
            'flag': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'people': ('django.db.models.fields.IntegerField', [], {}),
            'square': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['budgetelem']