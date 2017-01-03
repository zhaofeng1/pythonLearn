'''
Created on 2016年12月30日

@author: Administrator
'''
if __name__ == "__main__":
    print("程序自身运行")
else:
    print("另一模块")
    
def print_func( par ):
    if __name__ == "__main__":
        print ("Hello : ", par)
    else:
        print("Hello other:",par)
    return

def test_zf(test):
    return test

#print_func("test")

