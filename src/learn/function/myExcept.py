'''
Created on 2017年1月3日

@author: Administrator
'''
from learn.function.exceptionTest import MyError

try:
    raise MyError(2*2)
    print("b")
except MyError as err:
    print('My exception occurred, value:', err.value)
    
    
raise MyError("test")
