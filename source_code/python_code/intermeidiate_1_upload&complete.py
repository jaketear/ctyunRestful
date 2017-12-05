# coding: utf-8
#********no.1 multipart upload
import global_file
from global_file import global_path
import oosfunction
from oosfunction import HttpRequest

host="http://oos-bj2.ctyunapi.cn"
ak="58cc1dd2a52d5309a4f4"
sk="5ac5b36ef3a394a46a816b8d6e833badd30db7a8"
Upload=HttpRequest(host,ak,sk)
#upload part
chunksize=int(1024*1024*10)  #10M per part
path=global_path+u"source_code/A320 QRH REV43 0540.pdf"
bucketname="picture2"
objectname="example1.txt"
headers={"Content-Type":"string"}
files={}
subResource=""
PartNumber=0
with open(path,'rb') as f:
    while True:
        chunk=f.read(chunksize)
        if not chunk:
            break
        PartNumber+=1
        length=str(len(chunk))
        headers["Content-Lenth"]=length
        #use the uploadId get by init
        subResource="?partNumber="+str(PartNumber)+"&uploadId=1508491208226081142"
        payload={"partNumber":str(PartNumber),"uploadId":"1508491208226081142"}
        r=Upload.httpput(files,headers,payload,data=chunk,bucketname=bucketname,objectname=objectname,subResource=subResource)
        print r,r.headers,r.text,r.url

#complete upload
host="http://oos-bj2.ctyunapi.cn"
ak="58cc1dd2a52d5309a4f4"
sk="5ac5b36ef3a394a46a816b8d6e833badd30db7a8"
CompleteUpload=HttpRequest(host,ak,sk)
payload={"uploadId":"1508491208226081142"}
subResource="?uploadId=1508491208226081142"
bucketname="picture2"
objectname="example1.txt"
path=global_path+u"source_code/xmldata.txt"
with open(path,'rb') as xmldata:
    data=xmldata.read()
    length=len(data)
    headers={"Content-Length":str(length),"Content-Type":"text/xml"}
    r=CompleteUpload.httppost(files,headers,data,payload,host=host,bucketname=bucketname,objectname=objectname,subResource=subResource)
print r,r.headers,r.text,r.url
