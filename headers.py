#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2018/3/18 下午12:11
# Author  : Thomas Wang
# File    : headers.py
# Version : 1.0

import random

def generateRandomHeader():
    headerList = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
                  'Mozilla / 5.0(Windows NT 6.1; WOW64; rv:34.0) Gecko / 20100101 Firefox / 34.0',
                  'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
                  'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
                  'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16']
    header = headerList[random.randint(0,len(headerList)-1)]
    return header

