#!/usr/bin/python3
'''This is 11 question'''


class Student:

    '''Practice class'''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if attrs is None:
            return self.__dict__
        else:
            test = {}
            for a in attrs:
                try:
                    test[a] = self.__dict__[a]
                except Exception:
                    pass
            return test

    def reload_from_json(self, json):
        self.first_name = json.get('first_name', 'J')
        self.last_name = json.get('last_name', 'S')
        self.age = json.get('age', 1)
