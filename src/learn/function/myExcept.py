'''
Created on 2017年1月3日

@author: Administrator
'''
from learn.function.exceptionTest import MyError

try:
    raise MyError(2*2)
except MyError as err:
    print('My exception occurred, value:', err.value)
finally:
    print("over")
    
