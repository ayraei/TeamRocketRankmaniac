#!/usr/bin/env python

import sys

#
# This program generates the transition matrix and performs matrix
# multiplication on the distribution vector
#

adjList = []
trans = []
for line in sys.stdin:
    # Use the first pass of MapReduce to generate adjacency matrix
    # and rewrite data into desired format
    if True:
        adjList.append(line)
    else:
        sys.stdout.write(line)
