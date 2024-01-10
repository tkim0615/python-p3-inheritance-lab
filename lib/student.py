#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []
    
    def learn(self, string):
        self.knowledge.append(string)
        return self.knowledge
        

tyler = Student('tyler', 'kim')
print(tyler.first_name, tyler.knowledge)
    # Expand the learn() method in the Student class so that in takes in a
    #  string and adds that string
    #  to the student's self.knowledge list.