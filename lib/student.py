#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self):
        self.knowledge=[]
    
    def learn(self,mylist):
        self.knowledge.append(mylist)
        return self.knowledge
    


kimemia=Student()
print(kimemia.learn("kimemia"))

myname=[]
myname.append(["me","again"])
print(myname)    