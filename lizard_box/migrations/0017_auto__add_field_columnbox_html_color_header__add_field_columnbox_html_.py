# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'ColumnBox.html_color_header'
        db.add_column('lizard_box_columnbox', 'html_color_header', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True), keep_default=False)

        # Adding field 'ColumnBox.html_color_body'
        db.add_column('lizard_box_columnbox', 'html_color_body', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'ColumnBox.html_color_header'
        db.delete_column('lizard_box_columnbox', 'html_color_header')

        # Deleting field 'ColumnBox.html_color_body'
        db.delete_column('lizard_box_columnbox', 'html_color_body')


    models = {
        'lizard_box.box': {
            'Meta': {'ordering': "(u'name',)", 'object_name': 'Box'},
            'box_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'icon_class': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'template': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'lizard_box.column': {
            'Meta': {'ordering': "(u'layout', u'index')", 'object_name': 'Column'},
            'boxes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lizard_box.Box']", 'through': "orm['lizard_box.ColumnBox']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'layout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_box.Layout']"}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'lizard_box.columnbox': {
            'Meta': {'ordering': "(u'index',)", 'object_name': 'ColumnBox'},
            'action_boxes': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'action_boxes'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lizard_box.Box']"}),
            'box': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_box.Box']"}),
            'column': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_box.Column']"}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'html_color_body': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'html_color_header': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'maximize_action': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'refresh_millis': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'lizard_box.layout': {
            'Meta': {'object_name': 'Layout'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'portal_tabs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lizard_box.PortalTab']", 'through': "orm['lizard_box.LayoutPortalTab']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'lizard_box.layoutportaltab': {
            'Meta': {'ordering': "(u'index',)", 'object_name': 'LayoutPortalTab'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'layout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_box.Layout']"}),
            'portal_tab': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_box.PortalTab']"})
        },
        'lizard_box.portaltab': {
            'Meta': {'object_name': 'PortalTab'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'destination_slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'destination_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'icon_class': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'tab_type': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['lizard_box']
