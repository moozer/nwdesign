'''
Created on Jul 8, 2015

@author: moz

Inspiration/code from:
* https://gist.github.com/matthiaseisen/3278cedcd53afe62c3f3

'''

import functools
import graphviz as gv

class l2Graph(object):
    '''
    classdocs
    '''

    styles = {
        'graph': {
            'sep': '+25,25',
            'overlap': 'scale',
        },
        'nodes': {
            'shape': 'none',
            'labelloc': 'b',
        },
        'edges': {
            'color': 'black',
        }
    }
    iconPath="icons/"

    def apply_styles(self, styles):
        self._graph.graph_attr.update(
                                ('graph' in styles and styles['graph']) or {}
                                )
        self._graph.node_attr.update(
                               ('nodes' in styles and styles['nodes']) or {}
                               )
        self._graph.edge_attr.update(
                               ('edges' in styles and styles['edges']) or {}
                               )

    def add_nodes(self, nodes):
        for n in nodes:
            if isinstance(n, tuple):
                self._graph.node(n[0], **n[1])
            else:
                self._graph.node(n)
     
     
    def add_edges(self, edges):
        for e in edges:
            if isinstance(e[0], tuple):
                self._graph.edge(*e[0], **e[1])
            else:
                self._graph.edge(*e)

      

    def __init__( self, graphName ):
        '''
        Constructor
        '''
        self.name = graphName
        self._graph = functools.partial(gv.Graph, format='png', engine="neato")()
        self.apply_styles( self.styles)
        
    
    def addDevices(self, deviceConns):
        # aplphabetically sorted node list
        nodes = sorted( deviceConns.keys() )

        # first add all nodes
        for node in nodes:
            devType = deviceConns[node]['Device type']
            self.add_nodes( [(node, {'label': node, 'image': self.iconPath+"%s.png"%devType} ) ])
            
        # then add all edges (for readability)
        for node in nodes:
            for conn in deviceConns[node]['Interfaces']:
                remoteNode = conn['Remote device']
                if remoteNode > node:
                    labelText = "<<table BORDER='0'><tr><td BGCOLOR='white'>%s</td></tr></table>>"%conn['VLANs']
                    self.add_edges( [ ((node, remoteNode), {'label': labelText }) ] )
                #else already included
            
        pass

    @property    
    def dotText(self):
        return self._graph.source

    
    def generate(self):

        for engine in ['neato', 'fdp']:
            self._graph.engine = engine        
            self._graph.render( "%s.%s"%(self.name, engine) )

        self._graph.save( "%s.dot"%self.name )
        
        