'''
Created on 2016年12月30日

@author: Administrator
'''
#abs 绝对值
import math
print("abs(-12) :",abs(-12))
print("abs(120.0) :",abs(120.0))
print("abs(119L) :",abs(119))

#ceil向上取整
print("math.cell(-35.14):",math.ceil(-35.14))
print("math.cell(35.14):",math.ceil(35.14))
print("math.cell(pi):",math.ceil(math.pi))

#floor向下取整
print("math.floor(3.14):",math.floor(3.14))

#log 取对数
print("math.log(100):",math.log(100))
print("math.log10(100):",math.log10(100))

#max 
print("max(10,20,30):",max(10,20,30))

#round
print("round(10.54678,2):",round(10.54678,2))

import random

print ("从 range(100) 返回一个随机数 : ",random.choice(range(100)))
print ("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", random.choice([1, 2, 3, 5, 9]))
print ("从字符串中 'Runoob' 返回一个随机字符 : ", random.choice('Runoob'))






