#!/usr/bin/python3
'''Save Object to a file'''

import json


def save_to_json_file(my_list, text):

    '''Practice json file '''

    with open(text, 'w') as file:
        file.write(json.dumps(my_list))
