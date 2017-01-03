'''
Created on 2017年1月3日

@author: Administrator
'''

#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a 
        self.__weight = w 
    
    def speak(self):
        print("{0} 说: 我 {1} 岁。".format(self.name, self.age))
        
#实例化
p = people('tom',10,100)
p.speak()

