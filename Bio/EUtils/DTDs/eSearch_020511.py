#!/usr/bin/python

# This file generated by a program. do not edit.
import EUtils.POM

#     
#                 This is the Current DTD for Entrez eSearch
# $Id: eSearch_020511.py,v 1.1 2003-06-13 00:49:37 dalke Exp $
# 
#  ================================================================= 
class Count(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \d+ 
class RetMax(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \d+ 
class RetStart(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \d+ 
class Id(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \d+ 
class From(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class To(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class Term(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class Field(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class QueryKey(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \d+ 
class WebEnv(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \S+ 
class Explode(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  (Y|N) 
class OP(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  (AND|OR|NOT|RANGE) 
class IdList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'Id', u'*')], ''))


class Translation(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'From', ''), (u'To', '')], ''))


class TranslationSet(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'Translation', u'*')], ''))


class TermSet(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'Term', ''), (u'Field', ''), (u'Count', ''), (u'Explode', '')], ''))


class TranslationStack(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'|', [(u'TermSet', ''), (u'OP', '')], u'*')], ''))


#  Error message tags  
class ERROR(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class OutputMessage(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class QuotedPhraseNotFound(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class PhraseIgnored(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class FieldNotFound(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class PhraseNotFound(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class ErrorList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'PhraseNotFound', u'*'), (u'FieldNotFound', u'*')], ''))


class WarningList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'PhraseIgnored', u'*'), (u'QuotedPhraseNotFound', u'*'), (u'OutputMessage', u'*')], ''))


#  Response tags 
class eSearchResult(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'|', [(u',', [(u'Count', ''), (u',', [(u'RetMax', ''), (u'RetStart', ''), (u'QueryKey', u'?'), (u'WebEnv', u'?'), (u'IdList', ''), (u'TranslationSet', ''), (u'TranslationStack', u'?')], u'?')], ''), (u'ERROR', '')], ''), (u'ErrorList', u'?'), (u'WarningList', u'?')], ''))

