'''
Created on 2016年12月29日

@author: Administrator
'''

for l in 'Python':
    print("now letter:",l)
    
fruits = ['a','b','c']
for index in range(len(fruits)):
    print("now fruit:",fruits[index])
    
print("good bye!")

for num in range(10,20):
    for i in range(2,num):
        if num%i == 0:
            j=num/i
            print("%d 等于 %d * %d" % (num,i,j))
            break
    else:
        print(num,"是一个质数")

for x in range(0,3):
    print(x)



