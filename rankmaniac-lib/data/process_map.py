#!/usr/bin/env python

import sys

#
# This program does things.
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
colAdjList = []
distrVector = []
firstIteration = False
for line in sys.stdin:
    # Compute the transition matrix only on the first MapReduce iteration
    if 'NodeId' in line:
        firstIteration = True
        adjList.append(line)
    else:
        nodeId,iterNum = line.split()[0].split(';')
        colVal,adjCol = line.split()[1].split(';')
        if len(distrVector) == 0:
            distrVector = [0] * len(adjCol.split(','))
            colAdjList = [0] * len(adjCol.split(','))
        distrVector[nodeId] = colVal
        colAdjList[nodeId] = adjCol

if firstIteration:
    trans = get_P(adjList)
    for i in range(len(trans)):
        sys.stdout.write(i)
else:
    pass