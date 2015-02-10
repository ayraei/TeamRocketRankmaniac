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

### Here is some psuedocode for planning out map.
### For our transitional matrix, i guess the best way of using our map func
### would be to map the matrix multiplcation step, (at least that was the)
### (only thing i could think of to break up.)
### We could pass into map a key and a tuple of lists. the key is the index
### corresponding to our new r vector and the tuple could have the current r
### as a list and the second argument would be the relavent column from the P 
### matrix. The map would return the key and the value at the index for r(i+1)

### The reduce will then collect this list of values and keys and put them
### in order based on index to return our new r vector.

### we interatively call map-reduce and our current r value 50 times to get
### page rank.
