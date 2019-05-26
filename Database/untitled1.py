# -*- coding: utf-8 -*-
"""
Created on Sat May 25 20:55:37 2019

@author: Rajesh
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May 25 15:06:15 2019

@author: Rajesh
"""

import os,json
from datetime import datetime

class CustomError(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.value


class Database:
    def __init__(self,name,location=os.getcwd()):
        self.absloc=os.path.join(location,name+".json")
        self.key_value={}
        if os.path.isfile(self.absloc)==False:
            self.file=open(self.absloc,"w")
            json.dump(self.key_value,self.file)
        else:
            self.file=open(self.absloc,"r")

    def read(self,key):
        self.file=open(self.absloc,"r")
        self.key_value=json.load(self.file)
        try:
                if key in self.key_value:
                    print(self.key_value[key]['value'])
                else:
                    raise KeyError
        except KeyError:
            print("Read Fail: Key not Present")
        self.file.close()
            
    def update(self):
        self.file=open(self.absloc,"r")
        self.key_value=json.load(self.file)
        self.file.close()
        
    def create(self): 
        self.update()
        key=input()
        try:
            if key in self.key_value:
                raise KeyError
            if len(key)>2:
                raise CustomError("Size of Key should be less than 32 characters")
        except KeyError:
            print("Write Fail: Key already present")
        except CustomError as error:
            print(error.msg)
        else:
            value=json.dumps(input())
            ttl=int(input())
            self.file=open(self.absloc,"w")
            self.key_value[key]={"value":value,"ttl":ttl}
            json.dump(self.key_value,self.file)
        self.file.close()
    
    def delete(self,key):
        self.update()
        try:
            if key in self.key_value:
                del self.key_value[key]
                self.file=open(self.absloc,"w")
                json.dump(self.key_value,self.file)
            else:
                raise KeyError
        except KeyError:
            print("Delete Fail: Key not present")
        