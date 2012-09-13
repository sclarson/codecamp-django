# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Session.time'
        db.add_column('codecamp_session', 'time',
                      self.gf('django.db.models.fields.CharField')(default='8', max_length=2),
                      keep_default=False)

        # Adding field 'Session.room'
        db.add_column('codecamp_session', 'room',
                      self.gf('django.db.models.fields.IntegerField')(default=4),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Session.time'
        db.delete_column('codecamp_session', 'time')

        # Deleting field 'Session.room'
        db.delete_column('codecamp_session', 'room')


    models = {
        'codecamp.frontpagescroller': {
            'Meta': {'object_name': 'FrontpageScroller'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'codecamp.session': {
            'Meta': {'ordering': "['title']", 'object_name': 'Session'},
            'abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room': ('django.db.models.fields.IntegerField', [], {'default': '4'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'speakers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['codecamp.Speaker']", 'symmetrical': 'False'}),
            'time': ('django.db.models.fields.CharField', [], {'default': "'8'", 'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '2012'})
        },
        'codecamp.speaker': {
            'Meta': {'ordering': "['last_name']", 'object_name': 'Speaker'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'company_website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'codecamp.submittedsession': {
            'Meta': {'object_name': 'SubmittedSession'},
            'abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['codecamp']