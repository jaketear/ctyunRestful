# coding: utf-8
#**********no.2 change bucket acl(public)
import global_file
from global_file import global_path
import oosfunction
from oosfunction import HttpRequest

host="http://oos-bj2.ctyunapi.cn"
ak="58cc1dd2a52d5309a4f4"
sk="5ac5b36ef3a394a46a816b8d6e833badd30db7a8"
ChangeAcl=HttpRequest(host,ak,sk)
bucketname="picture1"
objectname=""
headers={"x-amz-acl":"public-read-write"}
payload={}
subResource=""
files={}
r=ChangeAcl.httpput(files,headers,payload,bucketname=bucketname,objectname=objectname,subResource=subResource)
print r,r.headers,r.text,r.url
