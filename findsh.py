#!/usr/bin/env python3
__author__='DGideas';
import os;
import sys;
import codecs;
import urllib.request;
import subprocess;

try:
	os.chdir(os.path.dirname(sys.argv[0]));
except FileNotFoundError:
	pass;
except OSError:
	pass;

i=1;
stri='';
while i<=5000:
	p=6-int(len(str(i)));
	stri=str(i);
	while p>1:
		stri='0'+str(stri);
		p=p-1;
	stri='6'+str(stri);
	#上证指数
	try:
		urllib.request.urlopen('http://203.90.242.126/list=sh'+str(stri)); #equal to hq.sinajs.cn
	except:
		print('Fetch an error, pass');
	else:
		info=urllib.request.urlopen('http://203.90.242.126/list=sh'+str(stri)); #equal to hq.sinajs.cn
		print(stri);
		strinfo=info.read();
		strinfo=strinfo.decode('gb2312')[0:-1];
		if len(strinfo.split(','))==1:
			print('^:Find no exist, skip');
		else:
			f=codecs.open('runtimesh.tmp','a','utf8');
			f.write(strinfo+'\n');
			f.close();
	i=i+1;
subprocess.call('rm -f runtimesh.csv',shell=True);
subprocess.call('mv runtimesh.tmp runtimesh.csv',shell=True);
