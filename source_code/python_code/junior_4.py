# coding: utf-8
#*********no.4:download object
import global_file
from global_file import global_path
import oosfunction
from oosfunction import HttpRequest

host="http://oos-bj2.ctyunapi.cn"
ak="58cc1dd2a52d5309a4f4"
sk="5ac5b36ef3a394a46a816b8d6e833badd30db7a8"
GetObject=HttpRequest(host,ak,sk)
headers={}
payload={}
files={}
bucketname="picture1"
objectname="%E7%9B%AE%E6%A0%871.txt"
subResource=""
r=GetObject.httpget(files,headers,payload,bucketname=bucketname,objectname=objectname,subResource=subResource)
print r,r.headers,r.text,r.url
with open(global_path+u'source_code/目标picture1.txt','wb') as code:
    code.write(r.content)
