'''
Created on 2017年1月3日

@author: Administrator
'''

for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3), end=" ")
    print(repr(x*x*x).rjust(4))
    
for x in range(1,11):
    print("{0:2d} {1:3d} {2:4d}".format(x,x*x,x*x*x))
    
str = input("请输入：")
print("你输入的是：",str)