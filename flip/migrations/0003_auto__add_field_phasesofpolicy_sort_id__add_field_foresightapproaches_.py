# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PhasesOfPolicy.sort_id'
        db.add_column(u'flip_phasesofpolicy', 'sort_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ForesightApproaches.sort_id'
        db.add_column(u'flip_foresightapproaches', 'sort_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True),
                      keep_default=False)

        # Adding field 'TypeOfOutcome.sort_id'
        db.add_column(u'flip_typeofoutcome', 'sort_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PhasesOfPolicy.sort_id'
        db.delete_column(u'flip_phasesofpolicy', 'sort_id')

        # Deleting field 'ForesightApproaches.sort_id'
        db.delete_column(u'flip_foresightapproaches', 'sort_id')

        # Deleting field 'TypeOfOutcome.sort_id'
        db.delete_column(u'flip_typeofoutcome', 'sort_id')


    models = {
        u'common.country': {
            'Meta': {'object_name': 'Country'},
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'common.environmentaltheme': {
            'Meta': {'ordering': "('-pk',)", 'object_name': 'EnvironmentalTheme'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'common.geographicalscope': {
            'Meta': {'ordering': "('-pk',)", 'object_name': 'GeographicalScope'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'require_country': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'flip.foresightapproaches': {
            'Meta': {'ordering': "('sort_id',)", 'object_name': 'ForesightApproaches'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'flip.language': {
            'Meta': {'object_name': 'Language'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'flip.outcome': {
            'Meta': {'object_name': 'Outcome'},
            'document_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'file_id': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'outcomes'", 'to': u"orm['flip.Study']"}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'type_of_outcome': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['flip.TypeOfOutcome']", 'null': 'True', 'blank': 'True'})
        },
        u'flip.phasesofpolicy': {
            'Meta': {'ordering': "('sort_id',)", 'object_name': 'PhasesOfPolicy'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'flip.study': {
            'Meta': {'object_name': 'Study'},
            'additional_information': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'additional_information_foresight': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'additional_information_phase': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'additional_information_stakeholder': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'blossom': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'countries': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['common.Country']", 'symmetrical': 'False', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'draft': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'environmental_themes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['common.EnvironmentalTheme']", 'symmetrical': 'False', 'blank': 'True'}),
            'foresight_approaches': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['flip.ForesightApproaches']", 'symmetrical': 'False'}),
            'geographical_scope': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.GeographicalScope']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'languages': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['flip.Language']", 'through': u"orm['flip.StudyLanguage']", 'symmetrical': 'False'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'lead_author': ('django.db.models.fields.TextField', [], {}),
            'other': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phase_of_policy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['flip.PhasesOfPolicy']", 'null': 'True', 'blank': 'True'}),
            'purpose_and_target': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'requested_by': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'stakeholder_participation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'study_type': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'})
        },
        u'flip.studylanguage': {
            'Meta': {'object_name': 'StudyLanguage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['flip.Language']"}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['flip.Study']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'flip.typeofoutcome': {
            'Meta': {'ordering': "('sort_id',)", 'object_name': 'TypeOfOutcome'},
            'blossom': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'doc_type': ('django.db.models.fields.CharField', [], {'default': "'all'", 'max_length': '128', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['flip']