# coding: utf-8
#*******no.9 delete AK/SK
import global_file
from global_file import global_path
import oosfunction
from oosfunction import HttpRequest

host="http://oos-bj2-iam.ctyunapi.cn"
ak="58cc1dd2a52d5309a4f4"
sk="5ac5b36ef3a394a46a816b8d6e833badd30db7a8"
DeleteAkSk=HttpRequest(host,ak,sk)
headers={}
files={}
subResource=""
payload={"Action":"DeleteAccessKey","AccessKeyId":"48dc71041105ce1e7bb0"}
data="Action=DeleteAccessKey&AccessKeyId=48dc71041105ce1e7bb0"
bucketname=""
objectname=""
r=DeleteAkSk.httppost(files,headers,data,payload,bucketname=bucketname,objectname=objectname,subResource=subResource)
print r,r.headers,r.text,r.url
