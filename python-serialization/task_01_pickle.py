#!/usr/bin/python3
'''Testing'''


import pickle


class CustomObject:
    '''Test'''

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):

        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Is Student: {self.is_student}')

    def serialize(self, filename):
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename: str):
        """Deserialize a CustomObject instance from a file using pickle."""
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)


            if isinstance(obj, cls):
                return obj
            return None

        except Exception:
            return None
