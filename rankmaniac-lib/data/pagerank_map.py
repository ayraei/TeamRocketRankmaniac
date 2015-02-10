#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

def get_P(adjList):
    """ Function to read the adj. list of a graph and return the transition
    matrix. 
    
    @param adjList list of strings in the format of NodeId:(node#)\tpagerank,
    oldpagerank, other node #s,
    example:
    NodeId:0\t1.0,0.0,1,3
    
    @ return returns a list of lists. Each element is a row in the trans 
    matrix. Sum of each row is 1.
    """
    P = []
    n = len(adjList)
    
    # get row for each node in the graph
    for node in adjList:
        
        row = [0] * n
        # get list of other nodes it connects to
        edges = node.split("\t")[1].split(",")[2:]
        # update values in row to be 1/n if node is connected
        for edg in edges:
            row[int(edg)] = (1.0 / len(edges))
        P.append(row)
    return P

adjList = []
trans = []
for line in sys.stdin:
    sys.stdout.write(line)
