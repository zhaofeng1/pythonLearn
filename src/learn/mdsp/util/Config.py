# coding=utf-8
'''
Created on 2017年3月6日

@author: Administrator
'''
class Config:
    
    class ConstError(TypeError): pass
    class ConstCaseError(ConstError): pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("can't change const %s" % name)
        if not name.isupper():
            raise self.ConstCaseError('const name "%s" is not all uppercase' % name)
        self.__dict__[name] = value

config = Config()
config.PI = 3.14
config.DBHOST = "10.200.10.149";
config.DBPORT = 3306;
config.DBUSER = "zhaofeng";
config.DBPWD = "123456";
config.DBNAME = "dsp_test_dev";
config.DBCHAR = "utf8";