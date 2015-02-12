#!/usr/bin/env python

'''
pagerank_map.py
    input: ((position=nodeId, iter_num), (distr_vector_col, col_of_adj_matrix))
    # do the matrix multiplication
    output: ((position=nodeId, iter_num), (col_val_in_new_st, col_of_adj_matrix))

process_map.py
    input: ((position=nodeId, iter_num), (col_val_in_new_st, col_of_adj_matrix))
    # reassemble the distribution vector and adjacency matrix(vertically instead)
    output: ((position=nodeId, iter_num), (distr_vector_col, col_of_adj_matrix))
'''

import sys
from matrix_mod import *



# This program does things.
#

adjCol = []
distrVector = []
firstIteration = False
finalIteration = False
printFlag = False
iterNum = 0
for line in sys.stdin:
    if 'NodeId' in line:
        firstIteration = True
        sys.stdout.write(line)
    elif 'FinalRank' in line:
        printFlag = True
        sys.stdout.write(line)
    else:
        nodeId,iterNum = line.split()[0].split(';')
        nodeId, iterNum = int(nodeId), int(iterNum)
        colVal,adjCol = line.split()[1].split(';')
        if len(distrVector) == 0:
            distrVector = [0] * len(adjCol.split(', '))
            colAdjList = [0] * len(adjCol.split(', '))
        distrVector[nodeId] = [float(x) for x in colVal[1:-1].split(', ')]
        colAdjList[nodeId] = [float(x) for x in adjCol[1:-1].split(', ')]

if firstIteration:
    pass
elif printFlag:
    pass
else:
    colVal = 0.0
   
    for num in range(len(distrVector)):
        colVal += (distrVector[num] * adjCol[num])
        sys.stdout.write('%d;%d\t%f;%s' % (num, iterNum, colVal, adjCol))

