'''
Created on 2016年12月30日

@author: Administrator
'''
import sys
def count(n):  
    print ("cunting" ) 
    while n > 0:  
        print ('before yield')  
        yield n   #生成值：n  
        n -= 1  
        print ('after yield' )
        yield 2


for i in count(5):  
    print (i)
    print("=====")
    
# 测试
c = count(3)
while True:
    try:
        print(next(c))
    except StopIteration:
        sys.exit()
        
        
        
        
        
        
        
