# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Books'
        db.create_table(u'bookseller_books', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ISBN', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal(u'bookseller', ['Books'])

        # Adding model 'Customers'
        db.create_table(u'bookseller_customers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'bookseller', ['Customers'])

        # Adding M2M table for field favorites on 'Customers'
        m2m_table_name = db.shorten_name(u'bookseller_customers_favorites')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customers', models.ForeignKey(orm[u'bookseller.customers'], null=False)),
            ('books', models.ForeignKey(orm[u'bookseller.books'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customers_id', 'books_id'])


    def backwards(self, orm):
        # Deleting model 'Books'
        db.delete_table(u'bookseller_books')

        # Deleting model 'Customers'
        db.delete_table(u'bookseller_customers')

        # Removing M2M table for field favorites on 'Customers'
        db.delete_table(db.shorten_name(u'bookseller_customers_favorites'))


    models = {
        u'bookseller.books': {
            'ISBN': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'Meta': {'object_name': 'Books'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'book': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'bookseller.customers': {
            'Meta': {'object_name': 'Customers'},
            'favorites': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bookseller.Books']", 'symmetrical': 'False'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['bookseller']