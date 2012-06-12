#!/usr/bin/python
import os
import sys
import commands
import optparse
import re
from os.path import join, getsize



def get_files(dir, pattern):
    size = 0L
    res = []
    for root,dir,files in os.walk(dir):
        for f in files:
            if f.endswith(pattern):
                res.append(join(root, f))
    return res


htmls = get_files("./", ".html")

def process(html_file):
    #pattern=re.compile('http:\/\/([\/\.][\w%]+)*\.(jpg|png|gif)'
    #pattern=re.compile('http:*\.jpg')
    pattern = re.compile('src="http:\/\/moorekang.+\..+zip"')
    f = open(html_file, "r")
    text = f.read()
    res = pattern.findall(text)
    if len(res) != 0:
        #print res
        for r in res:
            print r[4:-1]
            cmd = "wget " + r[5:-1]
            os.system(cmd)

for f in htmls:
    process(f)


#pattern = re.compile('http:\/\/.+\.(jpg|png)')
#pattern = re.compile('(https?:)?//?[^\'"<>]+?\.(jpg|jpeg|gif|png)')
#pattern = re.compile('\.png|\.jpg')
#res = pattern.findall("ahttp://c/b/a.jpg:http://c/x.png")
#print res
