#!/usr/bin/env python

import sys
from matrix_mod import *


#
# This program simply returns r1 given an adj list file
#

adj = []

for line in sys.stdin:
    # input should be a file with specified adj list format
    adj.append(line)
 
P = get_P(adj) # get the transition matrix

n = len(adj) # get dimensions of r1

r0 = [1.0/n] * n # intialize r0 to 1/n

r1 = mult_mat(r0,P)
sys.stdout.write(str(r1)) 

### Can modify this file further to take in r1 to make
### this function recursive or something


