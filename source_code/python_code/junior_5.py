# coding: utf-8
#*******no.5:shareurl
import global_file
from global_file import global_path
import datetime
import time
import requests
import oosfunction
from oosfunction import HttpRequest

host="http://oos-bj2.ctyunapi.cn"
ak="58cc1dd2a52d5309a4f4"
sk="5ac5b36ef3a394a46a816b8d6e833badd30db7a8"
ShareUrl=HttpRequest(host,ak,sk)
#headers={'Content-Type': 'bat'}
headers={}
files={}
subResource=""
payload=""
bucketname="picture1"
objectname="%E7%9B%AE%E6%A0%871.txt"
date=datetime.datetime.utcnow().strftime('%a, %d %b %Y %X +0000')

UrlShare=ShareUrl.urlshareobj("http://oos-bj2.ctyunapi.cn",headers,"GET",date,bucketname,objectname,"",7*24*60*60)
print "SharedUrl:"+UrlShare
#通过分享的url访问
r=requests.get(UrlShare,headers=headers,files=files,params=payload)
print r,r.headers,r.text,r.url

