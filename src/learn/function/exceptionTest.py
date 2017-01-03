'''
Created on 2017年1月3日

@author: Administrator
'''
class MyError(Exception):
    def __init__(self,value):
            self.value = value
    def __str__(self):
            return repr(self.value)