import sys
import json
import random


def cluster_lists(adj, num_groups):
    ''' Function that takes in the adjacency list and divides the nodes into 
    num_groups different cluster groups. 
    
    input is adj list from json file, num_groups an integer.
    
    output is a list of lists. Each inner list is a cluster of nodes.
    
    '''
    assert num_groups > 0
    
    # Add all of the nodes to a list of unclaimed nodes
    unused = []
    for key in adj:
        unused.append(int(key))
   
    # Then we randomly select Num_seed nodes as starting points for our cluster
    
    test_seeds = []
    
    clusters = []
    
    for i in range(num_groups):
        test_seeds.append(random.choice(unused))
        unused.remove(test_seeds[i])

    # Simulate the test nodes by expanding them into clusters from the test 
    # starts. Run the iterative process 3 times to select random nodes, test
    # resulting group sizes and eliminating the smallest nodes
    
    for iters in range(5):
    
        clusters = simulate(adj, test_seeds)
            
        clust_map = map(len,clusters)
        # search through the groups to find the smallest and largest group based on
        # test_seeds
        min_node = 0
        min_size = clust_map[0]
        max_size = clust_map[0]
        max_cluster = clusters[0]
    
        for i in range(1, len(clust_map)):
            if min_size > clust_map[i]:
                min_size = clust_map[i]
                min_node = i
            if max_size < clust_map[i]:
                max_size = clust_map[i] 
                max_cluster = clusters[i]
    
        while True:
            # select random nodes in the largest group until we find one that isn't
            # the original

            new_node = random.choice(max_cluster)
            if new_node not in test_seeds:
                break
            
            # remove the test_seed resulting in the smallest group and replace
                  # it with a random node in the largest group
                  
        test_seeds.remove(test_seeds[min_node])        
        test_seeds.append(new_node)

    clusters = simulate(adj, test_seeds)    
    #return map(len,clusters)
    clust_map = map(len,clusters)
 
    return clusters

def simulate(adj, test_seeds):
    '''
    Function to primitively simulate how nodes will spread given a graph and
    so many starting nodes
    
    '''
    # Add all of the nodes to a list of unclaimed nodes
    unused = []
    for key in adj:
        unused.append(int(key))
        
    clusters = []    
    
    for i in range(len(test_seeds)):
        clusters.append([test_seeds[i]])
        unused.remove(test_seeds[i])
    
    # Expand from our starting nodes, each iteration add all neighbors of a 
    # cluster to the cluster until all nodes are matched
    groups_to_search = range(len(clusters))
    
    while len(groups_to_search) != 0:
        
        start = len(unused)
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

def go_for_centrality(adj, num_groups, type_cen):
    ''' 
    Strategy to split our graph into groups or "clusters" and select the 
    highest centrality coefficient node for each group.
    '''
    
    # Pass each group into a function that returns the node with the highest
    # centrality coefficient.
    
    seeds = []
    clusters = cluster_lists(adj, num_groups)
 
    for group in clusters:
        seeds.append(degree_cen(adj, group))
        
    return seeds

def degree_cen(adj, group):
    '''
    Given a list of nodes and an adj list return the node number for the
    highest degree node.
    
    return is an integer
    '''
    assert len(group) > 0
    
    max_degree = 0
    max_node = -1
    
    # Go through each node in the group and check it's degree against the max
    for node in group:
        if len(adj[str(node)]) > max_degree:
            max_degree = len(adj[str(node)])
            max_node = node
            
    return max_node
        
    
def betweenness(adj, num):
    '''
    return the top nodes based on the betweenness 
    '''
    # make the adj matrix A based on the edges i,j
    import numpy
    A = []
    ALPHA = .25
    
    for _ in adj:
        A.append([0] * len(adj))
        
    for i in sorted(map(int,adj.keys())):
        for j in map(int, adj[str(i)]):
            A[i][j] = 1
            
    A_M = numpy.matrix(A)
            
    betweenness = []
    
    for i in range(len(adj)):
        print i
        katz = 0
        temp_A = 1
        temp_ALPHA = 1        
        for k in range(2): # calculate k up to distance 2 away
            temp_ALPHA = temp_ALPHA * ALPHA
            temp_A = temp_A * A_M    
            katz += temp_A[i].sum() * (temp_ALPHA)

        betweenness.append(katz)
        

    top_katz = []
    
    for i in range(num):
        max_D = 0
        max_Index = 0
        for i in range(len(betweenness)):
            if (betweenness[i] > max_D) and (i not in top_katz):
                max_D = betweenness[i]
                maxIndex = i    
        top_katz.append(maxIndex)
            
    return top_katz      