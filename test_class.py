#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 11:29:48 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

class Person(object):
    
    def __init__(self):
        
        self.firstName = "Yucheng"
        self.lastName = "Fang"
        self.ssn = None
        self.dob = None
        self.state = None
    
    def __str__(self):
        return self.firstName + " " + self.lastName
    
    def sayHello(self):
        print("Hello from " + self.firstName + self.lastName)
        
    def getFirstName(self):
        return self.firstName 
       
    def getLastName(self):
        return self.lastName
    
    def setFirstName(self, fname):
        self.firstName = fname
    
def main():
    p1 = Person()
    print(p1.firstName)

class Pig(Person):
    
    def test(self):
        pass

def main2():
    p1 = Pig()
    print(p1.firstName)

def main3():
    p1 = Pig()
    print(p1)

if __name__ == "__main__":
    main3()
    


# attribution and function
    
# class str