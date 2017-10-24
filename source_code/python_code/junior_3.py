# coding: utf-8
#**********no.3 put object
import global_file
from global_file import global_path
import oosfunction
from oosfunction import HttpRequest

host="http://oos-bj2.ctyunapi.cn"
ak="58cc1dd2a52d5309a4f4"
sk="5ac5b36ef3a394a46a816b8d6e833badd30db7a8"
PutObject=HttpRequest(host,ak,sk)
bucketname="picture1"
objectname="%E7%9B%AE%E6%A0%871.txt"
headers={"Content-Type":"text/plain"}   #Content-Type is required
subResource=""
#subResource="?response-content-encoding=utf-8"
payload={}
path=global_path+u"source_code/目标1.txt"
#files={'file':open(path,'rb')}
files={}
with open(path,'rb') as f:
    r=PutObject.httpput(files,headers,payload,data=f,bucketname=bucketname,objectname=objectname,subResource=subResource)
print r,r.headers,r.text,r.url
