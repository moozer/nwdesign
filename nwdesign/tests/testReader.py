'''
Created on Jul 7, 2015

@author: moz
'''
import unittest
from restIO import *
from restIO.restReader import *

filename = "somefile.rst"


class Test(unittest.TestCase):


    def testConstructor(self):
        r = restReader( filename )
        self.assertEqual( r.filename, filename )
        pass

    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()