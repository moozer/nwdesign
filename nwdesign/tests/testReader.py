'''
Created on Jul 7, 2015

@author: moz
'''
import unittest
from restIO import *
from restIO.restReader import *

filename = "data/basicNw.rst"
hwList = { "switch01": u'Switch01', "switch02": u'Switch02'}

class Test(unittest.TestCase):


    def testConstructor(self):
        r = restReader( filename )
        self.assertEqual( r.filename, filename )
        pass

    def testReadHardware(self):
        r = restReader( filename )
        self.assertEqual( r.hardwareList, hwList )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()