'''
Created on 2016年12月30日

@author: Administrator
'''
# 元组
from _collections import defaultdict
dictT = {"a":"apple","b":"banana","g":"grape","o":"orange"}
dictT["w"] = "watermelon"
del(dictT["a"])
dictT["g"] = "grapefruit"
print(dictT.pop("b"))
print(dictT)
print(dictT["o"])
print(dictT)

dictT.clear()
print(dictT)

#字典遍历
dictT = {"a":"apple","b":"banana","g":"grape","o":"orange"}
for k in dictT:
    print("dictT[%s]:" % k,dictT[k])
print(dictT.get("a"))
print("over1")

#字典items()的使用
dictT = {"a" : "apple", "b" : "banana", "c" : "grape", "d" : "orange"}
#每个元素是一个key和value组成的元组，以列表的方式输出
print(dictT.items())

test = [("a","testa"),("b","testb")]
print(test)
print(dict(test))
print("over")

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
        d[k].append(v)
   
print(s)
print(d)     
print("values:%s" % d.items())

for str in d.items():
    print(str)

dictT = {"a" : "apple", "b" : "banana", "c" : "grape", "d" : "orange"}  
#输出key列表
print(dictT.keys())
print(dictT.values())
print(dictT.items)

print("dict update=======")
dictT = {"a" : "apple", "b" : "banana"}
print(dictT)
dictT2 = {"c" : "grape", "a" : "orange"}
dictT.update(dictT2)
print(dictT)


print("dict set default=====")
#设置默认值
dictT = {}
dictT.setdefault("a")
print(dictT)
print(dictT["a"])
dictT["a"] = "apple"
dictT.setdefault("a","default")
print(dictT)

#调用sorted()排序
print("dict sorted=========")
dictT = {"b" : "grape", "c" : "orange", "d" : "banana","a" : "apple"}
print(dictT)
print(sorted(dictT.items(), key=lambda d:d[0]))
#按照value排序 
print(sorted(dictT.items(), key=lambda d: d[1]))

print(sorted(dictT))


#字典的浅拷贝
print("cict copy============")
dictT = {"a" : "apple", "b" : "grape"}
dictT2 = {"c" : "orange", "d" : "banana"}
dictT2 = dictT.copy()
print(dictT2)

# 初始化
print("dict init ===========")
d = dict(name='visaya', age=20)
print(d)
d = dict(zip(['name', 'age'], ['visaya', 201]))
print(d)

#dict.fromkeys(listkeys, default=0) 把listkeys中的元素作为key均赋值为value，默认为0
d = dict.fromkeys(['a', 'b'], 1)
print(d)

