# coding: utf-8
#***********Thread list&get&delete
import global_file
from global_file import global_path
import oosfunction
from oosfunction import httpput
from oosfunction import httpget
from oosfunction import httpdelete
from oosfunction import MyThread
import xml.etree.ElementTree as ET

#******list object
bucketname="picture3"
files={}
payload={"prefix":"Feb/"}
headers={}
objectname=""
subResource=""
r=httpget(files,headers,payload,bucketname=bucketname,objectname=objectname,subResource=subResource)
with open(global_path+u'source_code/listobject.xml','wb') as f:
    f.write(r.content)
print r,r.headers,r.text,r.url


#******multithreading get object
host="http://oos-bj2.ctyunapi.cn"
bucketname="picture3"
subResource=""
objectnamelist=[] #list存储需要get的object
payload={}
#获取xml文件中的Key标签值，get这些Key值对应的object
tree=ET.parse(global_path+u'source_code/listobject.xml')
root=tree.getroot()#获得root节点
xmlns='{http://s3.amazonaws.com/doc/2006-03-01/}'#xml namespace
for contents in root.findall(xmlns+'Contents'):#find Contents in xml
    key=contents.find(xmlns+'Key').text#find Key in Contents
    objectnamelist.append(key)
Threadnum=len(objectnamelist)
print Threadnum
#multhreading get
threadsget=[]#Thread list
for ig in range(Threadnum):
    tg=MyThread(httpget,args=({},{},payload,host,bucketname,objectnamelist[ig],subResource))
    threadsget.append(tg)
for tg in threadsget:
    tg.setDaemon(True)
    tg.start()
for tg in threadsget:
    tg.join()
    print tg.get_object(),tg.get_object().headers,tg.get_object().text,tg.get_object().url

#*******multi-threading delete other object
bucketname="picture3"
payload={}
headers={}
objectname=""
subResource=""
#get all object in bucket to varify delete object
r=httpget(files,headers,payload,bucketname=bucketname,objectname=objectname,subResource=subResource)
with open(global_path+u'source_code/listallobject.xml','wb') as f:
    f.write(r.content)
print r,r.headers,r.text,r.url

treeall=ET.parse(global_path+u'source_code/listallobject.xml')
rootall=treeall.getroot()#获得root节点
xmlns='{http://s3.amazonaws.com/doc/2006-03-01/}'
objectnamealllist=[]    #bucket的所有object
for contentsall in rootall.findall(xmlns+'Contents'):
    keyall=contentsall.find(xmlns+'Key').text
    objectnamealllist.append(keyall)
Threadnumall=len(objectnamealllist)
print Threadnumall
objectdellist=list(set(objectnamealllist)-set(objectnamelist))#not prefixed objectlist,which is to delete
Threadnumdel=len(objectdellist)
print objectdellist
threadsdelete=[]
for idt in range(Threadnumdel):
    td=MyThread(httpdelete,args=({},{},payload,host,bucketname,objectdellist[idt],subResource))
    threadsdelete.append(td)
for td in threadsdelete:
    td.setDaemon(True)
    td.start()
for td in threadsdelete:
    td.join()
    print td.get_result(),td.get_result().headers,td.get_result().text,td.get_result().url

