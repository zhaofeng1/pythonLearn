'''
Created on 2016年12月30日

@author: Administrator
'''
a = {"a":"apple","b":"banana"}
for k,v in a.items():
    print(k,":",v)
    
a = {"a":"apple","b":"banana"}
for i,v in enumerate(a):
    print(i,":",v)
    
a = {"a":"apple","b":"banana"}
b = {"c":"cfruit","d":"dfruit"}
for p,k in zip(a,b):
    print(a[p],"==",b[k])
    
    
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
print(basket)
for f in sorted(set(basket)):
    print(f)
    
# 多种排序方法    
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'A', 20),('dave', 'C', 20)]  
sortage = sorted(students, key=lambda student : student[2])# sort by age 
print(sortage)
students.sort()
print(students)
students.sort(reverse=True)  #reverse True：倒序   False：正序  默认为false
print(students)
students.sort(key=lambda x:x[1], reverse=True)
print(students)

import operator
students.sort(key=operator.itemgetter(0), reverse=False)
print(students)

students.sort(key=operator.itemgetter(2,1), reverse=False) #先按第三个 再按第二个
print(students)













































