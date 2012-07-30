# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Layout'
        db.create_table('lizard_box_layout', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
        ))
        db.send_create_signal('lizard_box', ['Layout'])

        # Adding model 'Column'
        db.create_table('lizard_box_column', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('layout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_box.Layout'])),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('index', self.gf('django.db.models.fields.IntegerField')(default=100)),
        ))
        db.send_create_signal('lizard_box', ['Column'])

        # Adding model 'Box'
        db.create_table('lizard_box_box', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal('lizard_box', ['Box'])

        # Adding model 'ColumnBox'
        db.create_table('lizard_box_columnbox', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('box', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_box.Box'])),
            ('column', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_box.Column'])),
            ('index', self.gf('django.db.models.fields.IntegerField')(default=100)),
        ))
        db.send_create_signal('lizard_box', ['ColumnBox'])


    def backwards(self, orm):
        
        # Deleting model 'Layout'
        db.delete_table('lizard_box_layout')

        # Deleting model 'Column'
        db.delete_table('lizard_box_column')

        # Deleting model 'Box'
        db.delete_table('lizard_box_box')

        # Deleting model 'ColumnBox'
        db.delete_table('lizard_box_columnbox')


    models = {
        'lizard_box.box': {
            'Meta': {'object_name': 'Box'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'lizard_box.column': {
            'Meta': {'object_name': 'Column'},
            'boxes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lizard_box.Box']", 'through': "orm['lizard_box.ColumnBox']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'layout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_box.Layout']"}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'lizard_box.columnbox': {
            'Meta': {'object_name': 'ColumnBox'},
            'box': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_box.Box']"}),
            'column': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_box.Column']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        },
        'lizard_box.layout': {
            'Meta': {'object_name': 'Layout'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['lizard_box']
