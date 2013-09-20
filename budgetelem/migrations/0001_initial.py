# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BElem'
        db.create_table('budgetelem_belem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('budgetelem', ['BElem'])

        # Adding model 'CodesProfit'
        db.create_table('budgetelem_codesprofit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('deep', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('budgetelem', ['CodesProfit'])

        # Adding model 'Document'
        db.create_table('budgetelem_document', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('docfile', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('sheet_number', self.gf('django.db.models.fields.IntegerField')()),
            ('code_column', self.gf('django.db.models.fields.IntegerField')()),
            ('name_column', self.gf('django.db.models.fields.IntegerField')()),
            ('amount_column', self.gf('django.db.models.fields.IntegerField')()),
            ('start_budget', self.gf('django.db.models.fields.IntegerField')()),
            ('finish_budget', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('budgetelem', ['Document'])


    def backwards(self, orm):
        # Deleting model 'BElem'
        db.delete_table('budgetelem_belem')

        # Deleting model 'CodesProfit'
        db.delete_table('budgetelem_codesprofit')

        # Deleting model 'Document'
        db.delete_table('budgetelem_document')


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
            'code_column': ('django.db.models.fields.IntegerField', [], {}),
            'docfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'finish_budget': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_column': ('django.db.models.fields.IntegerField', [], {}),
            'sheet_number': ('django.db.models.fields.IntegerField', [], {}),
            'start_budget': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['budgetelem']