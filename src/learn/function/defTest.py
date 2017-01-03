'''
Created on 2016年12月30日

@author: Administrator
'''
def area(width,height):
    return width*height

print("width:",10,"height:",2,"area:",area(10, 2))

for i in range(4):
    print(i)
    
matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
print(matrix)
result = []
for i in range(4):
    temp = []
    for row in matrix:
        temp.append(row[i])
    #print(temp)
    result.append(temp) #添加新对象
    #result.extend(temp) #扩展
print(result)