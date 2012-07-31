# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'PortalTab'
        db.create_table('lizard_box_portaltab', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tab_type', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('destination_slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('destination_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('lizard_box', ['PortalTab'])

        # Adding model 'LayoutPortalTab'
        db.create_table('lizard_box_layoutportaltab', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('layout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_box.Layout'])),
            ('portal_tab', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_box.PortalTab'])),
            ('index', self.gf('django.db.models.fields.IntegerField')(default=100)),
        ))
        db.send_create_signal('lizard_box', ['LayoutPortalTab'])

        # Changing field 'Box.url'
        db.alter_column('lizard_box_box', 'url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))


    def backwards(self, orm):
        
        # Deleting model 'PortalTab'
        db.delete_table('lizard_box_portaltab')

        # Deleting model 'LayoutPortalTab'
        db.delete_table('lizard_box_layoutportaltab')

        # Changing field 'Box.url'
        db.alter_column('lizard_box_box', 'url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))


    models = {
        'lizard_box.box': {
            'Meta': {'object_name': 'Box'},
            'box_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'icon_class': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'template': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
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
            'action_boxes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'action_boxes'", 'symmetrical': 'False', 'to': "orm['lizard_box.Box']"}),
            'box': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_box.Box']"}),
            'column': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_box.Column']"}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'})
        },
        'lizard_box.layout': {
            'Meta': {'object_name': 'Layout'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'portal_tabs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lizard_box.PortalTab']", 'through': "orm['lizard_box.LayoutPortalTab']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'lizard_box.layoutportaltab': {
            'Meta': {'object_name': 'LayoutPortalTab'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'layout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_box.Layout']"}),
            'portal_tab': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_box.PortalTab']"})
        },
        'lizard_box.portaltab': {
            'Meta': {'object_name': 'PortalTab'},
            'destination_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'destination_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tab_type': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['lizard_box']
