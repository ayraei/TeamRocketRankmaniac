#!/usr/bin/env python

import sys

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
    alpha = 0.85
    
    # get row for each node in the graph
    for node in adjList:
        
        row = [float((1-alpha)/n)] * n
        # get list of other nodes it connects to
        edges = node.split("\t")[1].split(",")[2:]
        # update values in row to be 1/n if node is connected
        for edg in edges:
            row[int(edg)] += (alpha / len(edges))
        P.append(row)
    return P

adjList = []
colAdjList = []
distrVector = []
firstIteration = False
finalIteration = False
printFlag = False
for line in sys.stdin:
    # Compute the transition matrix only on the first MapReduce iteration
    if 'NodeId' in line:
        firstIteration = True
        adjList.append(line)
    # Last iteration
    elif 'FinalRank' in line:
        printFlag = True
        sys.stdout.write(line)
    # Neither first nor last
    else:
        nodeId,iterNum = line.split('\t')[0].split(';')
        nodeId, iterNum = int(nodeId), int(iterNum)
        # Begin the final iteration
        if iterNum >= 49:
            finalIteration = True
        colVal,adjCol = line.split('\t')[1].split(';')
        if len(distrVector) == 0:
            distrVector = [0] * len(adjCol.split(', '))
            colAdjList = [0] * len(adjCol.split(', '))
        distrVector[nodeId] = float(colVal)
        colAdjList[nodeId] = [float(x) for x in adjCol[1:-2].split(', ')]

if firstIteration:
    trans = get_P(adjList)
    n = len(trans)
    for i in range(n):
        col = []
        # build the transition matrix by column
        for row in trans:
            col.append(row[i])
        distrVector = [1.0/n] * n
        sys.stdout.write('%d;%d\t%s;%s\n' % (i, 1, distrVector, col))
elif finalIteration:
    for i in range(min(len(distrVector), 20)):
        sys.stdout.write('FinalRank:%f\t%d\n' % (distrVector[i], i))
elif printFlag:
    pass
else:
    for i in range(len(colAdjList)):
        sys.stdout.write('%d;%d\t%s;%s\n' % (i, iterNum+1, distrVector, colAdjList[i]))