'''
Created on Jul 7, 2015

@author: moz
'''

import docutils.parsers.rst
import docutils.utils.new_document

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
    
    def parseFile(self):
        with open(self.filename) as f:
            parser = docutils.parsers.rst.Parser()
            settings = docutils.frontend.OptionParser(
                components=(docutils.parsers.rst.Parser,)
                ).get_default_values()
            document = docutils.utils.new_document(self.filename, settings)
            parser.parse(f, document)
            
            print parser.document
            