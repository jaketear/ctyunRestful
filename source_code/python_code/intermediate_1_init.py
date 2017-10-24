# coding: utf-8
#********no.1 multipart upload
#initial
import global_file
from global_file import global_path
import oosfunction
from oosfunction import httpput
from oosfunction import httppost

headers={"Content-Type":""}
files={}
subResource="?uploads"
payload="uploads"
data=""
host="http://oos-bj2.ctyunapi.cn"  #change default host
bucketname="picture2"
objectname="example1.txt"
r=httppost(files,headers,data,payload,host=host,bucketname=bucketname,objectname=objectname,subResource=subResource)
with open(global_path+u'source_code/multipart_upload.txt','wb') as code:
    code.write(r.content)
print r,r.headers,r.text,r.url


