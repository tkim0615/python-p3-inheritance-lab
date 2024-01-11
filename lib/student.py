#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []


    def learn(self, new_info):
        self.knowledge.append(new_info)
        return self.knowledge


student1 = Student('Tyler', 'Kim')
print(student1.first_name)
print(student1.learn('python is fun'))