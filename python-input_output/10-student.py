#!/usr/bin/python3
'''Student to JSON with filter'''


class Student:
    '''Practice json'''

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
                    if self.__dict__[a]:
                        test[a] = self.__dict__[a]
                except Exception:
                    pass
            return test
