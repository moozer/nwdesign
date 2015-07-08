'''
Created on Jul 7, 2015

@author: moz
'''

import docutils.parsers.rst
from docutils import utils
from docutils import core


class restReader(object):
    '''
    classdocs
    '''


    def __init__(self, filename):
        '''
        Constructor
        '''
        self._filename = filename
        self._parseFile()
        self._hwEntry = None
        self._hwEntryIds = "hardware-devices"
        
    @property
    def filename(self):
        return self._filename
    
    def _parseFile(self):
        with open(self.filename) as f:
            parser = docutils.parsers.rst.Parser()
            settings = docutils.frontend.OptionParser(
                components=(docutils.parsers.rst.Parser,)
                ).get_default_values()
            self._document = docutils.utils.new_document(self.filename, settings)
            parser.parse( f.read(), self._document )
            
    @property
    def hardwareList(self):
        # find the hardware list section
        if not self._hwEntry:
            for subdoc in self._document.traverse(condition=docutils.nodes.section):
                if subdoc.attributes['ids'][0] == self._hwEntryIds:
                    self._hwEntry = subdoc
                    break
    
        # if still nothing
        if not self._hwEntry:
            print "failed to find hardware device list section named %s"%self._hwEntryIds
            return None
        
        devList = {}
        for section in self._hwEntry.traverse(condition=docutils.nodes.section):
            if section.attributes['ids'][0] == self._hwEntryIds:
                continue
            devList[section.attributes['ids'][0]] = section.children[0].children[0]

        return devList

