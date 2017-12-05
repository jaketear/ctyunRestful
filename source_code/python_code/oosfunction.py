# coding: utf-8
import global_file
from global_file import global_path
import hmac
import hashlib
import base64
import datetime
import time
import requests
import json
import threading
import xml.etree.ElementTree as ET

#重写Thread类
class MyThread(threading.Thread):  
    def __init__(self,func,args=()):
        super(MyThread,self).__init__()
        self.func=func
        self.args=args
    def run(self):
        self.result=self.func(*self.args)  #tuple
    def get_result(self):
        try:
            return self.result
        except Exception:
            return None
    def get_object(self):
        try:
            with open(global_path+u'source_code/'+self.getName()+'.txt','wb') as f:
                f.write(self.result.content)
            return self.result
        except Exception:
            return None

class HttpRequest:
    def __init__(self,host,ak,sk):
        self.host=host
        self.ak=ak
        self.sk=sk
    def url_create(self,host="",bucket="",objectname="",subResource=""):
        if(host==""):
            host=self.host
        myurl=host+"/"+bucketname+"/"+objectname+subResource
        return myurl
    def urlshareobj(self,host="",headers={},httpverb="GET",date="",bucketname="",objectname="",subResource="",ValidTime=0):
        if(host==""):
            host=self.host
        #ak="58cc1dd2a52d5309a4f4"
        UnixTime=str(int(time.time())+ValidTime)
        authorization=self.authorize(headers,httpverb,UnixTime,bucketname,objectname,subResource) #Expires replace date
        #print authorization
        begin=authorization.find(":")
        signature=authorization[begin+1:] #get signature from authorization
        ShareParams={"Expires":UnixTime,"AWSAccessKeyId":self.ak,"Signature":signature}
        myurl=host+"/"+bucketname+"/"+objectname
        #req=requests.PreparedRequest.prepare(method=httpverb,url=myurl,headers=headers,params=ShareParams)
        req=requests.PreparedRequest()
        req.prepare_url(myurl,ShareParams)
        return req.url
    # x-amz-头标准化构建
    def CanonilizedAMZHeaders_Create(self,headers):
        HeaderStringList=[]
        HeaderString=""
        for k in headers.keys():
            HeaderKey=k.rstrip().lower()
            if(HeaderKey.startswith("x-amz-")):
                HeaderValue=headers[k].lstrip()
                count=0
                i=0
                while i<len(HeaderStringList):
                    if(HeaderStringList[i].startswith(HeaderKey+":")):
                        HeaderStringList[i]+=","+HeaderValue
                        print HeaderStringList
                        count+=1
                    i+=1
                if(count==0):
                    HeaderStringList.append(HeaderKey+":"+HeaderValue)
        HeaderStringList.sort()
        for s in HeaderStringList:
            HeaderString+=s+"\n"
        print HeaderString   #for display
    
        return HeaderString
            
    def authorize(self,headers={},httpverb="GET",date="",bucketname="",objectname="",subResource=""):
        #ak="58cc1dd2a52d5309a4f4"
        #sk="5ac5b36ef3a394a46a816b8d6e833badd30db7a8"
        Content_Type=""
        if(headers.get("Content-Type")):
            Content_Type=headers.get("Content-Type")
        Content_MD5=""
        if(headers.get("Content-MD5")):
            Content_Type=headers.get("Content-MD5")
        CanonilizedAMZHeaders=self.CanonilizedAMZHeaders_Create(headers)
        if(bucketname!=""):
            StringToSign=httpverb+"\n"+Content_MD5+"\n"+Content_Type+"\n"+date+"\n"+CanonilizedAMZHeaders+"/"+bucketname+"/"+objectname+subResource
        else:
            StringToSign=httpverb+"\n"+Content_MD5+"\n"+Content_Type+"\n"+date+"\n"+CanonilizedAMZHeaders+"/"+subResource
        signature=hmac.new(self.sk,StringToSign,hashlib.sha1).digest()
        signature= base64.b64encode(signature)
        #signature=hmac.new(sk.encode('utf-8'),StringToSign.encode('utf-8'),hashlib.sha1).digest().encode('base64').rstrip()
        authorization="AWS "+self.ak+":"+signature
        return authorization

    def usersignature(self,policydict={}):
        
        #policy='{"expiration": "2017-10-28T12:00:00.000Z", "conditions": [{"bucket":"picture2"}, ["start-with", "$key", "user/eric/"], {"acl":"public-read"}]}'
        policy=json.dumps(policydict)
        policy_base64=base64.b64encode(policy)
        #sk="5ac5b36ef3a394a46a816b8d6e833badd30db7a8"
        signature_user=hmac.new(self.sk,policy_base64,hashlib.sha1).digest()
        signature_user= base64.b64encode(signature_user)
        return policy_base64,signature_user

    def httpput(self,files,headers,payload,data="",host="",bucketname="",objectname="",subResource=""):
        if(host==""):
            host=self.host
        date=datetime.datetime.utcnow().strftime('%a, %d %b %Y %X +0000')
        #use requests params add to url or directly add subResource to url
        #myurl=host+"/"+bucketname+"/"+objectname+subResource
        if(bucketname!=""):
            myurl=host+"/"+bucketname+"/"+objectname
        else:
            myurl=host+"/"
        authorization=self.authorize(headers,"PUT",date,bucketname,objectname,subResource)
        headers["Date"]=date
        headers["Authorization"]=authorization
        r=requests.put(myurl,data=data,headers=headers,files=files,params=payload)
        return r


    def httpget(self,files,headers,payload,host="",bucketname="",objectname="",subResource=""):
        if(host==""):
            host=self.host
        date=datetime.datetime.utcnow().strftime('%a, %d %b %Y %X +0000')
        #use requests params add to url or directly add subResource to url
        #myurl=host+"/"+bucketname+"/"+objectname+subResource
        if(bucketname!=""):
            myurl=host+"/"+bucketname+"/"+objectname
        else:
            myurl=host+"/"
        authorization=self.authorize(headers,"GET",date,bucketname,objectname,subResource)
        headers["Date"]=date
        headers["Authorization"]=authorization
        r=requests.get(myurl,headers=headers,files=files,params=payload)
        return r

    def httpdelete(self,files,headers,payload,host="",bucketname="",objectname="",subResource=""):
        if(host==""):
            host=self.host
        date=datetime.datetime.utcnow().strftime('%a, %d %b %Y %X +0000')
        #use requests params add to url or directly add subResource to url
        #myurl=host+"/"+bucketname+"/"+objectname+subResource
        if(bucketname!=""):
            myurl=host+"/"+bucketname+"/"+objectname
        else:
            myurl=host+"/"
        authorization=self.authorize(headers,"DELETE",date,bucketname,objectname,subResource)
        headers["Date"]=date
        headers["Authorization"]=authorization
        r=requests.delete(myurl,headers=headers,files=files,params=payload)
        return r

    def httppost(self,files,headers,data,payload,host="",bucketname="",objectname="",subResource=""):
        if(host==""):
            host=self.host
        date=datetime.datetime.utcnow().strftime('%a, %d %b %Y %X +0000')
        #use requests params add to url or directly add subResource to url
        #myurl=host+"/"+bucketname+"/"+objectname+subResource
        if(bucketname!=""):
            myurl=host+"/"+bucketname+"/"+objectname
        else:
            myurl=host+"/"
        authorization=self.authorize(headers,"POST",date,bucketname,objectname,subResource)
        headers["Date"]=date
        headers["Authorization"]=authorization
        r=requests.post(myurl,data=data,headers=headers,files=files,params=payload)
        return r
