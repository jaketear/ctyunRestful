# coding: utf-8
#*******no.8 update AK/SK(Primary)
import global_file
from global_file import global_path
import oosfunction
from oosfunction import HttpRequest

host="http://oos-bj2-iam.ctyunapi.cn"
ak="58cc1dd2a52d5309a4f4"
sk="5ac5b36ef3a394a46a816b8d6e833badd30db7a8"
UpdateAkSk=HttpRequest(host,ak,sk)
headers={"Content-Type":"string"}
files={}
subResource=""
payload={"Action":"UpdateAccessKey","AccessKeyId":"e8d1f88e8f37da5152b5","Status":"active","IsPrimary":"true"}
data=payload  #when data is dict type,headers must be user defined
bucketname=""
objectname=""
r=UpdateAkSk.httppost(files,headers,data,payload,bucketname=bucketname,objectname=objectname,subResource=subResource)
print r,r.headers,r.text,r.url

#note:action is worked as data post to oos, params does't work(add to url)
