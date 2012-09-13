# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Speaker'
        db.create_table('codecamp_speaker', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('company_website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('codecamp', ['Speaker'])

        # Adding model 'Session'
        db.create_table('codecamp_session', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('abstract', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(default=2012)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('codecamp', ['Session'])

        # Adding M2M table for field speakers on 'Session'
        db.create_table('codecamp_session_speakers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('session', models.ForeignKey(orm['codecamp.session'], null=False)),
            ('speaker', models.ForeignKey(orm['codecamp.speaker'], null=False))
        ))
        db.create_unique('codecamp_session_speakers', ['session_id', 'speaker_id'])

        # Adding model 'SubmittedSession'
        db.create_table('codecamp_submittedsession', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('abstract', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
        ))
        db.send_create_signal('codecamp', ['SubmittedSession'])

        # Adding model 'FrontpageScroller'
        db.create_table('codecamp_frontpagescroller', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('codecamp', ['FrontpageScroller'])


    def backwards(self, orm):
        # Deleting model 'Speaker'
        db.delete_table('codecamp_speaker')

        # Deleting model 'Session'
        db.delete_table('codecamp_session')

        # Removing M2M table for field speakers on 'Session'
        db.delete_table('codecamp_session_speakers')

        # Deleting model 'SubmittedSession'
        db.delete_table('codecamp_submittedsession')

        # Deleting model 'FrontpageScroller'
        db.delete_table('codecamp_frontpagescroller')


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
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'speakers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['codecamp.Speaker']", 'symmetrical': 'False'}),
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