#!/usr/bin/python
# coding:utf8

"""
this module reads strings.csv, which contains all
the strings, and lets the main app use it 
"""

import csv
from flask import Markup

import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('webvectors.cfg')

root = config.get('Files and directories', 'root')
l10nfile = config.get('Files and directories', 'l10n')

# the encoding to use
encoding = 'utf8'

# open the strings database:
csvfile = open(root + l10nfile, 'rU')
acrobat = csv.reader(csvfile, dialect='excel', delimiter=',')

# initialize a dictionary for each language:
language_dicts = {}
for langname in acrobat.next()[1:]:
    language_dicts[langname] = {}

# read the csvfile, populate language_dicts:
for row in acrobat:
    for i in range(1, len(row)):
        # Markup() is used to prevent autoescaping in templates
        language_dicts[language_dicts.keys()[i - 1]][row[0]] = Markup(row[i].decode(encoding))
