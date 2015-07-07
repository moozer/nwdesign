'''
Created on Jul 7, 2015

@author: moz
'''

class restReader(object):
    '''
    classdocs
    '''


    def __init__(self, filename):
        '''
        Constructor
        '''
        self._filename = filename
        
    @property
    def filename(self):
        return self._filename