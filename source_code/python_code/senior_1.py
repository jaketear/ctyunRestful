# coding: utf-8
#********no.1 set redundancy put
import global_file
from global_file import global_path
import oosfunction
from oosfunction import httpput


bucketname="picture2"
objectname="%E7%9B%AE%E6%A0%87.txt"
subResource=""
payload={}
headers={"Content-Type":"text/txt","x-amz-storage-class":"EC_2_1_2"}
path=global_path+u"source_code/plan.txt"
#files={'file':open(path,'rb')} #also can use files put, but this will add content-disposition to files
files={}
with open(path,'rb') as f:
    data=f.read()
    r=httpput(files,headers,payload,data=data,bucketname=bucketname,objectname=objectname,subResource=subResource)
print r,r.headers,r.text,r.url
