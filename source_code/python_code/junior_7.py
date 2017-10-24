# coding: utf-8
#*******no.7 create AK/SK(default)
import global_file
from global_file import global_path
import oosfunction
from oosfunction import HttpRequest

host="http://oos-bj2-iam.ctyunapi.cn"
ak="58cc1dd2a52d5309a4f4"
sk="5ac5b36ef3a394a46a816b8d6e833badd30db7a8"
CreateAkSk=HttpRequest(host,ak,sk)
headers={}
subResource=""
files={}
payload={"Action":"CreateAccessKey"}
data="Action=CreateAccessKey"
bucketname=""
objectname=""
r=CreateAkSk.httppost(files,headers,data,payload,bucketname=bucketname,objectname=objectname,subResource=subResource)
with open(global_path+u'source_code/aksk.txt','wb') as code:
    code.write(r.content)

print r,r.headers,r.text,r.url
