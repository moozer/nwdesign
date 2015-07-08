'''
Created on Jul 7, 2015

@author: moz
'''
import unittest
from restIO import *
from restIO.restReader import *

filename = "data/basicNw.rst"
hwList = { "switch01": u'Switch01', "switch02": u'Switch02'}
deviceIds = "switch01"
deviceInfo = { 'Device type': "switch", 'Model': "HP procurve 1810",
               'Interfaces': [
                      { 'Interface': "1", "VLANs": "Default, SRV (T)", 
                      'Remote device': "Switch02",
                      'Remote interface': "1",
                      'Comments': ""},
                      { 'Interface': "2", "VLANs": "SRV", 
                      'Remote device': "",
                      'Remote interface': "",
                      'Comments': ""}
              ]}


class Test(unittest.TestCase):


    def testConstructor(self):
        r = restReader( filename )
        self.assertEqual( r.filename, filename )
        pass

    def testReadHardware(self):
        r = restReader( filename )
        self.assertEqual( r.hardwareList, hwList )
        
    def testGetDeviceInfo(self):
        r = restReader( filename )
        self.assertEqual( r.getDeviceInfo(deviceIds), deviceInfo )
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()