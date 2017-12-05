# coding: utf-8
#********no.1 multipart upload
#initial
import global_file
from global_file import global_path
import oosfunction
from oosfunction import HttpRequest

host="http://oos-bj2.ctyunapi.cn"
ak="58cc1dd2a52d5309a4f4"
sk="5ac5b36ef3a394a46a816b8d6e833badd30db7a8"
InitUpload=HttpRequest(host,ak,sk)
headers={"Content-Type":""}
files={}
subResource="?uploads"
payload="uploads"
data=""
bucketname="picture2"
objectname="example1.txt"
r=InitUpload.httppost(files,headers,data,payload,host=host,bucketname=bucketname,objectname=objectname,subResource=subResource)
#save UploadId to file 'multipart_upload'
with open(global_path+u'source_code/multipart_upload.txt','wb') as code:
    code.write(r.content)
print r,r.headers,r.text,r.url


