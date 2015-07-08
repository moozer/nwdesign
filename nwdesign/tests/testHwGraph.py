'''
Created on Jul 8, 2015

@author: moz
'''
import unittest
from graphOut.l2Graph import l2Graph
import os


deviceNameA = "Switch01"
deviceA = { 'Device type': "switch", 'Model': "HP procurve 1810",
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

deviceNameB = "Switch02"
deviceB = { 'Device type': "switch", 'Model': "HP procurve 1810",
               'Interfaces': [
                      { 'Interface': "1", "VLANs": "Default, SRV (T)", 
                      'Remote device': "Switch01",
                      'Remote interface': "1",
                      'Comments': ""},
                      { 'Interface': "2", "VLANs": "SRV", 
                      'Remote device': "",
                      'Remote interface': "",
                      'Comments': ""}
              ]}

deviceConns = { deviceNameA: deviceA, deviceNameB: deviceB }
graphName = "testout"
graphOut = '''graph {
\tgraph [overlap=scale sep="+50,50"]
\tnode [labelloc=b shape=none]
\tedge [color=black]
\t\tSwitch01 [label=Switch01 image="icons/switch.png"]
\t\tSwitch02 [label=Switch02 image="icons/switch.png"]
\t\t\tSwitch01 -- Switch02 [label=<<table BORDER='0'><tr><td BGCOLOR='white'>Default, SRV (T)</td></tr></table>>]
}'''
graphFilenameNeatoPng = "%s.neato.png"%graphName
graphFilenameFdpPng = "%s.fdp.png"%graphName
graphFilenameDot = "%s.dot"%graphName

class Test(unittest.TestCase):

    def setUp(self):
        files = [graphFilenameNeatoPng, graphFilenameFdpPng, graphFilenameDot]

        for f in files:            
            if os.path.isfile(f):
                os.remove(f)

    def testL2Graph(self):
        g = l2Graph(graphName)
        g.addDevices( deviceConns )
        self.assertEqual( g.dotText, graphOut )
        pass

    def testL2GraphGenerate(self):
        g = l2Graph(graphName)
        g.addDevices( deviceConns )
        g.generate()
        self.assertTrue( os.path.isfile(graphFilenameNeatoPng) )
        self.assertTrue( os.path.isfile(graphFilenameFdpPng) )
        self.assertTrue( os.path.isfile(graphFilenameDot) )        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testL2Graph']
    unittest.main()