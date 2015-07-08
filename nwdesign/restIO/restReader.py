'''
Created on Jul 7, 2015

@author: moz
'''

import docutils.parsers.rst
from docutils import utils
from docutils import core
import copy

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

    def _findHwEntry(self):
        for subdoc in self._document.traverse(condition=docutils.nodes.section):
            if subdoc.attributes['ids'][0] == self._hwEntryIds:
                self._hwEntry = subdoc
                break
    
        # if still nothing
        if not self._hwEntry:
            print "failed to find hardware device list section named %s"%self._hwEntryIds

            
    @property
    def hardwareList(self):
        ''' return the list of devices written in the "Hardware devices section"
        '''
        # find the hardware list section
        if not self._hwEntry:
            self._findHwEntry()
        
        devList = {}
        for section in self._hwEntry.traverse(condition=docutils.nodes.section):
            if section.attributes['ids'][0] == self._hwEntryIds:
                continue
            # section.children[0] is <title>...</title>
            # section.children[0].children[0] is the "..." between title
            devList[section.attributes['ids'][0]] = section.children[0].children[0]

        return devList


    def _readFieldList(self, nodeFieldList ):
        ''' parses the fieldlist and returns a dictionary
        '''
        retval = {}
        for field in nodeFieldList:
            # field -> fieldName -> raw text
            fieldName = field[0].rawsource
            # field -> fieldBody -> para graph entry -> raw text 
            fieldBody = field[1][0].rawsource
            retval[fieldName] = fieldBody
        
        return retval
    
    
    def _readTable(self, node):
        ''' node is a table node and the content is extracted as a 
            list of dictionaries
        '''
        entriesList = []

        # node -> tgroup -> thead -> row
        headerNode = node[0][-2][0]
        
        # extracting headers
        headerList = []
        for colname in headerNode:
            # entry -> paragraph -> text
            rawText = colname[0][0].rawsource
            header = rawText.replace( '\n', " ")
            headerList.append( header )
            
        #print headerList

        # node -> tgroup -> tbody
        rowNodes = node[0][-1]

        # go through all entries in table
        for rowNum in range(0, len(rowNodes) ):
            entriesDict = {}
            for colNum in range( 0, len(headerList) ):
                # row -> col -> paragraph -> raw text
                tableEntry = rowNodes[rowNum][colNum]
                entriesDict[headerList[colNum]] = tableEntry[0].rawsource if len(tableEntry) > 0 else ""

            # store dictionary in list
            entriesList.append( copy.deepcopy( entriesDict ) )
        
        print entriesList
        return entriesList
    
    
    def getDeviceInfo(self, deviceId):
        ''' returns the content of the table for the specific device
        '''
        # find the hardware list section
        if not self._hwEntry:
            self._findHwEntry()        
        
        # loop through devices until match
        deviceSec = None
        for section in self._hwEntry.traverse(condition=docutils.nodes.section):
           if section.attributes['ids'][0] == deviceId:
               deviceSec = section

        # children[0] is title - skipping
        fieldDict = {}
        connDict = {}
        for node in deviceSec:
            if node.tagname == "field_list":
                fieldDict = self._readFieldList(node)
            elif node.tagname == "table":
                interfaceList = self._readTable( node )
            elif node.tagname == "title":
                pass
            else:
                print "warning: unused tagname %s below id %s"%(node.tagname, deviceId )
            
        fieldDict["Interfaces"] = interfaceList

        return fieldDict