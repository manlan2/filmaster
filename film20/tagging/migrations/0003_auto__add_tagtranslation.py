# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TagTranslation'
        db.create_table('tagging_tagtranslation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pl', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True, null=True, blank=True)),
            ('en', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True, null=True, blank=True)),
        ))
        db.send_create_signal('tagging', ['TagTranslation'])


    def backwards(self, orm):
        
        # Deleting model 'TagTranslation'
        db.delete_table('tagging_tagtranslation')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'tagging.tag': {
            'LANG': ('django.db.models.fields.CharField', [], {'default': "'pl'", 'max_length': '2'}),
            'Meta': {'ordering': "('name',)", 'unique_together': "(('name', 'LANG'),)", 'object_name': 'Tag'},
            'category': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'tagging.tagalias': {
            'Meta': {'object_name': 'TagAlias'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tagging.Tag']"})
        },
        'tagging.taggeditem': {
            'Meta': {'unique_together': "(('tag', 'content_type', 'object_id'),)", 'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': "orm['tagging.Tag']"})
        },
        'tagging.tagtranslation': {
            'Meta': {'object_name': 'TagTranslation'},
            'en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pl': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tagging']
