#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2018/3/18 00:46
# Author  : Thomas Wang
# File    : PornHub.py
# Version : 1.0

import time
import urllib2
from bs4 import BeautifulSoup
import httplib
import random
from headers import generateRandomHeader

httplib.HTTPConnection._http_vsn = 10
httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'


def getUrlList(page):
    req = urllib2.Request('https://www.pornhub.com/video?page=%s' %page)
    req.add_header('user-agent', generateRandomHeader())
    try:
        html = urllib2.urlopen(req, timeout=30).read()
        return html
    except:
        html = urllib2.urlopen(req, timeout=30).read()
        return html


corpus = open('corpus1.txt', 'w')
startTime = time.time()
for i in range(1, 5331):
    print 'page', i, 'start crawling...'
    time.sleep(1+random.random())
    soup = BeautifulSoup(getUrlList(i), 'lxml')
    for j in soup.select('div.nf-videos ul li span.title a'):
            item = j.string.encode('ascii', 'ignore')
            # print item
            # print >> corpus, item
endTime = time.time()
timeUsed = endTime - startTime
print 'Program finished in ', timeUsed, 's'
corpus.close()

<div class=nf-videos>
    <ul>

    </ul>
</div>