#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:21:22 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

class Foo(object):
    counter = 0
    
    def __init__(self,a,b):
        self.x=a
        self.y=b
        self.id = Foo.counter
        self.__class__.counter += 1
    
    def main():
        object1=Foo("Object","Mars")
        object2=Foo("Object","Moon")
        print(object1.id,object1.x,object1.y)
        print(object2.id,object2.x,object2.y)      

class Person():
    counter = 0
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.personid = self.__class__.counter + 1

    def getFullName():
        return self.firstName + self.lastName
    
    def getPerson():
        return self.personid

test = Person(firstName="John", lastName="KKK")
p = test.getPerson()
print(p)