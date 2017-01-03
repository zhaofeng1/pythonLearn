'''
Created on 2016年12月30日

@author: Administrator
'''
# List
import sys
list1 = ["a","b","c"]
list1.append("f")
print(list1)

str1 = (12,"a","b")
list1 = list(str1)
print(list1)

print(range(5))

for i in range(5):
    print(i,end=",")

for i in range(3,5):
    print(i,end=",")  
    
list(range(5))
print(list(range(5)))  

#迭代
list1=[1,2,3,4]
it = iter(list1)
for x in it:
    print(x,end=" ")


list1=[1,2,3,4]
it = iter(list1)   
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()















