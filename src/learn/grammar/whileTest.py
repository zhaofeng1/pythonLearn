'''
Created on 2016年12月29日

@author: Administrator
'''

numbers = [12,37,5,42,8,3]
even = []
odd = []
num = 0
while len(numbers)>0 :
    num = numbers.pop()
    if num%2 ==0 :
        even.append(num)
    else:
        odd.append(num)
print("even:",even)
print("odd:",odd)
print("numbers:",numbers)

#flag = 1

#while (flag): print('Given flag is really true!')

#print("Good bye!")

#2~100之间的素数
i = 2
flag = False
while(i<100):
    j=2
    flag = False
    while(j<i):
        if(i%j==0):
            flag = True
            break
        j = j+1
    if(not flag):
        print(i,"是素数")
    i = i+1
            
print("bye")

for i in range(0,10):
    if not(i%2):
        print(i,"可被2整除")
    else:
        print(":::",i)
        
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数 
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b #右边的表达式先执行（=右边，由左向右执行）
#    print("a:",a)
#    print("b:",b)

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b





