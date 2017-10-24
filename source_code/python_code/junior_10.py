# coding: utf-8
#*******no.10 delete bucket
import global_file
from global_file import global_path
import oosfunction
from oosfunction import HttpRequest

host="http://oos-bj2.ctyunapi.cn"
ak="58cc1dd2a52d5309a4f4"
sk="5ac5b36ef3a394a46a816b8d6e833badd30db7a8"
DeleteBucket=HttpRequest(host,ak,sk)
headers={}
files={}
subResource=""
payload={}
bucketname="picture1"
objectname=""
r=DeleteBucket.httpdelete(files,headers,payload,bucketname=bucketname,objectname=objectname,subResource=subResource)
print r,r.headers,r.text,r.url
