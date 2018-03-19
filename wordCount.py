#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2018/3/18 下午6:16
# Author  : Thomas Wang
# File    : wordCount.py
# Version : 1.0

import collections
from processedText import wordList


def wordFilter():
    del raw['and']
    del raw['or']
    del raw['with']
    del raw['in']
    del raw['on']
    del raw['a']
    del raw['an']
    del raw['the']
    del raw['to']
    del raw['for']
    del raw['by']
    del raw['my']
    del raw['his']
    del raw['her']
    del raw['your']
    del raw['their']
    del raw['our']
    del raw['is']
    del raw['at']
    del raw['she']
    del raw['he']
    del raw['me']
    del raw['you']
    del raw['i']
    del raw['are']
    del raw['it']
    del raw['get']
    del raw['all']
    del raw['have']
    del raw['has']
    del raw['off']
    del raw['give']
    del raw['gets']
    del raw['get']
    del raw['gives']
    del raw['out']
    del raw['after']
    del raw['this']
    del raw['that']
    del raw['one']
    del raw['not']
    del raw['over']
    del raw['before']
    del raw['so']
    del raw['as']
    del raw['does']
    del raw['be']
    del raw['him']
    del raw['do']
    del raw['just']
    del raw['de']
    del raw['when']
    del raw['got']
    del raw['will']
    del raw['d']
    del raw['what']
    del raw['la']
    del raw['during']
    del raw['who']
    del raw['where']
    del raw['why']
    del raw['go']
    del raw['being']
    del raw['let']
    del raw['ca']
    del raw['n']
    del raw['too']
    del raw['w']
    del raw['about']
    del raw['but']
    del raw['was']
    del raw['am']
    del raw['they']
    del raw['e']
    del raw['we']
    del raw['g']
    del raw['would']
    del raw['should']
    del raw['if']
    del raw['t']
    del raw['und']
    del raw['le']
    del raw['im']
    del raw['y']
    del raw['j']
    del raw['l']
    del raw['m']
    del raw['th']
    del raw['c']
    del raw['put']
    del raw['plus']
    del raw['r']
    del raw['did']
    del raw['da']
    del raw['et']
    del raw['can']
    del raw['of']
    del raw['se']
    del raw['from']
    del raw['next']
    del raw['vs']


raw = collections.Counter(wordList)
wordFilter()
for i in raw.keys():
    if raw[i] < 100:
        raw.pop(i)
print raw

results = open('results.txt', 'w')
print results
results.close()



