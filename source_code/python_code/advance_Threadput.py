# coding: utf-8
#**********multi-threading put
import global_file
from global_file import global_path
import oosfunction
from oosfunction import HttpRequest
from oosfunction import MyThread
#multi-threading put

host="http://oos-bj2.ctyunapi.cn"
ak="58cc1dd2a52d5309a4f4"
sk="5ac5b36ef3a394a46a816b8d6e833badd30db7a8"
Multithread=HttpRequest(host,ak,sk)
data=""
bucketname="picture3"
payload={}
subResource=""

threads=[]
pathlist=[global_path+'source_code/threading/a1.txt',global_path+'source_code/threading/a2.txt',global_path+'source_code/threading/a3.txt']
data=[]
with open(pathlist[0],'rb') as f1:
    data.append(f1.read())
with open(pathlist[1],'rb') as f2:
    data.append(f2.read())
with open(pathlist[2],'rb') as f3:
    data.append(f3.read())
    
headerslist=[{"Content-Type":"text/txt"},{"Content-Type":"text/txt"},{"Content-Type":"text/txt"}]
filenamelist=["Feb/a1.txt","Feb/a2.txt","Aug/a3.txt"]
for i in range(3):
    t=MyThread(Multithread.httpput,args=({},headerslist[i],payload,data[i],host,bucketname,filenamelist[i],subResource))
    threads.append(t)
for t in threads:
    t.setDaemon(True)
    t.start()
for t in threads:
    t.join()
    print t.get_result(),t.get_result().headers,t.get_result().text,t.get_result().url
