'''
Created on 2016年12月29日

@author: Administrator
'''

flag = False
name = 'luren'
if name == 'python':
    flag = True
    print('welcome')
else:
    print(name)
    
print(flag)

num = 3
if num == 3:
    print("boss")
elif num == 2:
    print("user")
elif num == 1:
    print("work")
elif num < 0:
    print("error")
else:
    print("roadman")