# coding=utf-8
'''
Created on 2017年3月7日

@author: Administrator
'''
import MySQLdb

if __name__ == '__main__':
    # 打开数据库连接
    db = MySQLdb.connect("10.200.10.149","zhaofeng","123456","dsp_test_dev" )
    
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    
    # 使用execute方法执行SQL语句
    cursor.execute("SELECT VERSION()")
    
    # 使用 fetchone() 方法获取一条数据库。
    data = cursor.fetchone()
    
    print "Database version : %s " % data
    # 关闭数据库连接
    db.close()