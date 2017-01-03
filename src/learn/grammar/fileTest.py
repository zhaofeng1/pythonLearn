'''
Created on 2017年1月3日

@author: Administrator
'''
filePath = 'E:/crawler/python.txt'

# 打开文件
f = open(filePath, "r")
#lines = f.readlines()
#print(lines)

for line in f:
    print(line,end='')
    
f.close()
print("over")

import sys

# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise

try:
    f =  open(filePath)
    s = f.readline()

except OSError as err:
    print("OS error:{0}".format(err))
    
#....
with open(filePath) as f:
    for line in f:
        print(line,end="")
    

