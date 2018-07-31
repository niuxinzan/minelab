# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 14:08
# @Author  : buf
# @Email   : niuxinzan@cennavi.com.cn
# @File    : test_get_set.py
# @Software: PyCharm
#-*-encoding:utf-8-*-
class Person():
    # 只允许拥有私有的name和age属性
    __slots__ = ('__name', '__age')
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age
    def __str__(self):
        return '姓名 '+self.__name+' \n年龄'+str(self.__age)
if __name__=='__main__':
    zhangsan=Person('张三',20)
    print(zhangsan)
    print(zhangsan.name)
    print(zhangsan.age)
    zhangsan.age=30
    zhangsan.name='张三三'
    print(zhangsan)