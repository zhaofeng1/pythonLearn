'''
Created on 2016年12月30日

@author: Administrator
'''
basket = {"a","b","c","d","a"}
print(basket)
print(len(basket))

s = set('beginman')
print(s)
for i in s:
    print(i,end=" ")

s = frozenset("acdddb")
print(s)

a = {"a","b","c","c"}
b = {"c","d","e"}
print(a | b)
print(a - b)
print(a & b)
print(a ^ b)


    

    
    
