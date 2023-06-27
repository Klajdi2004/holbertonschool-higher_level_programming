#!usr/bin/python3
''' models/base.py
'''

import json

class Base:
    '''first class base
    '''
    
    __nb_objects = 0

    def __init__(self,id=None):
        ''' initialize base __init__
        '''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

