#!/usr/bin/python
import urllib2
import shutil

url = "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt"
fin = urllib2.urlopen(url)
shutil.copy("/home/ubd/.aria2/aria2.conf.bak","/home/ubd/.aria2/aria2.conf")
fout = open("/home/ubd/.aria2/aria2.conf","a")
allLine = 'bt-tracker='
for line in fin:
	if len(line) > 1:
		line=line.strip('\n')
		line=line+","
		allLine=allLine+line
allLine=allLine.strip(',')
fout.write(allLine)		
		

