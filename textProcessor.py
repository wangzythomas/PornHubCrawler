#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2018/3/18 下午4:58
# Author  : Thomas Wang
# File    : textProcessor.py
# Version : 1.0

import re
import collections
import nltk
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


def txtFilter(text):
    patLetter = re.compile(r'[^a-zA-Z \']+')
    new_text = patLetter.sub(' ', text).strip().lower()
    return new_text

def deAbbrIs(text):
    pat_is = re.compile("(it|he|she|that|this|there|here)(\'s)", re.I)
    new_text = pat_is.sub(r"\1 is", text)
    return new_text

def deAbbr(new_text):
    pat_s = re.compile("(?<=[a-zA-Z])\'s")
    pat_s2 = re.compile("(?<=s)\'s?")
    pat_not = re.compile("(?<=[a-zA-Z])n\'t")
    pat_would = re.compile("(?<=[a-zA-Z])\'d")
    pat_will = re.compile("(?<=[a-zA-Z])\'ll")
    pat_am = re.compile("(?<=[I|i])\'m")
    pat_are = re.compile("(?<=[a-zA-Z])\'re")
    pat_ve = re.compile("(?<=[a-zA-Z])\'ve")

    new_text = pat_s.sub("", new_text)
    new_text = pat_s2.sub("", new_text)
    new_text = pat_not.sub(" not", new_text)
    new_text = pat_would.sub(" would", new_text)
    new_text = pat_will.sub(" will", new_text)
    new_text = pat_am.sub(" am", new_text)
    new_text = pat_are.sub(" are", new_text)
    new_text = pat_ve.sub(" have", new_text)
    new_text = new_text.replace('\'', ' ')
    return new_text


# def get_wordnet_pos(treebank_tag):
#     if treebank_tag.startswith('J'):
#         return wordnet.ADJ
#     elif treebank_tag.startswith('V'):
#         return wordnet.VERB
#     elif treebank_tag.startswith('N'):
#         return wordnet.NOUN
#     elif treebank_tag.startswith('R'):
#         return wordnet.ADV
#     else:
#         return ''


processedText = open('processedText.py', 'w')
allWords = []
count = 0
with open('corpus1.txt') as f:
    for line in f:
        count += 1
        allWords.extend(deAbbr(deAbbrIs(txtFilter(line))).split( ))
        print 'finished line', count
print >> processedText, allWords

processedText.close()

# for i in range(len(allWords)):
#     allWords[i] = lemmatizer.lemmatize(allWords[i])
# print allWords
