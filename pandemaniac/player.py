#!/usr/bin/python


'''
Python Script to generate a strategy based on a graph.

CS144 Project Pandemaniac

Main function will take in as input the graph in the JSON format and return
print to the standard output the 10 nodes that should be used. Different
strategies will be written in as different functions and flags can be given when
calling the script to specify which strategy to generate seed nodes for.

USAGE:  >>  python player.py graphs.txt 1
 prints out the top ten nodes

'''
import sys
import json
import random
def get_degree_list(adj):
    ''' Helper function that returns a list of degrees based on the adj list.
    The output is a list of degree size with the index corresponding to the 
    node number.
    
    Input is a dictionary in json form, ex for a square graph, 
    {
    "0": ["1", "3"],
    "1": ["0", "2"],
    "2": ["1", "3"],
    "3": ["0", "2"]
    }
    '''
    degree = []
    
    for key in sorted(map(int,adj.keys())):
        degree.append(len(adj[str(key)]))
        
    return degree
    
    
def get_top_list(deg_list):
    ''' Helper function that returns a list of the highest degree nodes.
    
    Input is a list of the degrees based on index, see get_degree_list

    Output is a list with nodes indecies in order of degree size
    '''
    top_deg = []
    
    for i in range(len(deg_list)):
        max_D = 0
        max_Index = 0
        for i in range(len(deg_list)):
            if (deg_list[i] > max_D) and (i not in top_deg):
                max_D = deg_list[i]
                maxIndex = i    
        top_deg.append(maxIndex)
        
    return top_deg

def basic_strategy_1(adj):
    ''' Basic strategy example for pandemaniac. Other functions should follow
    this format. Basic strategy 1 simply returns the top 10 nodes with highest
    degree based on the graph.
    
    Input is an adjacency list in json format.
    
    Output is a list of 10 nodes to use as the seed nodes.'''
    
    top = get_top_list(get_degree_list(adj))
    
    return top[:NUM_SEEDS]

def basic_strategy_2(adj):
    ''' Basic strategy example for pandemaniac. Other functions should follow
    this format. Basic strategy 1 simply returns the top 5 nodes and the highest
    degree neighbor for each of those nodes. This is designed to beat the TA 
    team
    
    Input is an adjacency list in json format.
    
    Output is a list of 10 nodes to use as the seed nodes.'''
    
    deg_list = (get_degree_list(adj))
    
    top = get_top_list(deg_list)
    
    seeds = top[:NUM_SEEDS / 2]
    
    # get the highest degree neighbor for each top seed.
    for i in range(5):
        key = "%d" % i
        max_D = 0
        max_key = -1
        # Loop to get the max neighbor
        for neighbor in adj[key]:
            if deg_list[int(neighbor)] > max_D and int(neighbor) not in seeds:
                max_D = deg_list[int(neighbor)]
                max_key = int(neighbor)
            
        # Error if no seed was found
        if max_key == -1:
            raise KeyError()
        # Add the highest neighbor to the seeds list
        seeds.append(max_key)
    
    return seeds

def cluster_lists(adj, num_groups):
    ''' Function that takes in the adjacency list and divides the nodes into 
    num_groups different cluster groups. 
    
    input is adj list from json file, num_groups an integer.
    
    output is a list of lists. Each inner list is a cluster of nodes.
    
    '''
    
    # Add all of the nodes to a list of unclaimed nodes
    unused = []
    for key in adj:
        unused.append(int(key))
   
    # Then we randomly select Num_seed nodes as starting points for our cluster
    
    clusters = [[]] * NUM_SEEDS
    
    for i in range(len(clusters)):
        rand_node = random.choice(unused)
        clusters[i].append(rand_node)
        unused.remove(rand_node)
        
    
    # Expand from our starting nodes, each iteration add all neighbors of a 
    # cluster to the cluster until all nodes are matched
    groups_to_search = range(len(clusters))
    while len(unused) != 0:
        
        for index in groups_to_search:
            new_nodes = []
            for node in clusters[index]:
                for neighbor in adj[str(node)]:
                    if int(neighbor) in unused:
                        new_nodes.append(int(neighbor))
                        unused.remove(int(neighbor))
            clusters[index] += new_nodes
            if new_nodes == []:
                groups_to_search.remove(index)
        
    return clusters

def go_for_top_3(adj):
    ''' Strategy where the pandemic will aim for the top three degree nodes.
    Assuming the competion will cancel out the top nodes, this strategy aims to
    secure the highest degree node by surrounding it with out seeds.
    
    Goes for the top 3 nodes by picking the four highest degree neighbors for
    the top node, and the three highest degree neighbors for the 2nd and 3rd 
    hightest nodes.
    
    STILL WORK IN PROGRESS
    '''
    deg_list = get_degree_list(adj)
    top = get_top_list(deg_list)[:3]
    plan = []
    
    # find the top 4 nodes from node 0
    for i in range(4):
        max_D = 0
        for node in adj[str(top[0])]:
            if (deg_list[int(node)] > max_D) and int(node) not in plan:
                max_D = deg_list[int(node)]
                maxIndex = node
        plan.append(maxIndex)
    # find the top 3 nodes from node 1
    for i in range(3):
        max_D = 0
        for node in adj[str(top[1])]:
            if (deg_list[int(node)] > max_D) and int(node) not in plan:
                max_D = deg_list[int(node)]
                maxIndex = node
        plan.append(maxIndex)
    # find the top 3 nodes from node 2
    for i in range(3):
        max_D = 0
        for node in adj[str(top[2])]:
            if (deg_list[int(node)] > max_D) and int(node) not in plan:
                max_D = deg_list[int(node)]
                maxIndex = node
        plan.append(maxIndex)           
    
    
    return plan[:NUM_SEEDS]


# Python Script

# set the strategy to use
VALID_STARTEGIES = []
STRATEGY = 1
NUM_GAMES = 2 # number of games we select nodes for
NUM_SEEDS = 10 # number of seeds needed for each game

json_file = sys.argv[1]

# if a second argument is given use that strategy
if len(sys.argv) > 2:
    STRATEGY = int(sys.argv[2])

# open the file and create an adj list
data = []
with open(json_file) as f:
    for line in f:
        data.append(json.loads(line))
        
seed = []
STRATEGY_LIST = []
# Pick which strategy to use, ADD TO HERE ONLY IF THEY HAVE BEEN TESTED
# OTHERWISE WILL BE REPLACED WITH 1-10 (TODO)

if STRATEGY >= 1:
    STRATEGY_LIST.append(basic_strategy_2(data[0]))

if STRATEGY >= 2:
    pass

if STRATEGY >= 3:
    pass

STRATEGY_LIST.append(basic_strategy_1(data[0]))


seed = []
count = 0
i = 0

for game_num in range(NUM_GAMES):
    seed += STRATEGY_LIST[i]
    i = (i + 1) % len(STRATEGY_LIST)    
        
for node in seed:
    print node

    
