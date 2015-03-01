'''
Coded by Joanne Li, <joanne@caltech.edu>

The idea behind this strategy:
1) pick nodes that are all connected to each other in order to
   create a sort of "super node" that will be able to resist
   other players' advances by each voting for each other to keep
   our team's color. start the search at the node with
   the (NUM_SEEDS+1) highest degree (to increase chances of not
   being cancelled out by other teams' choices) and add all of its
   neighbors to our list of seed nodes to return, then iterate
   through this ever-growing list until we have enough seeds, or
   until we run out of neighbors.
2) if, for some reason, we run out of neighbors to pick, default
   to picking the remaining seeds out of the NUM_SEEDS nodes with
   the highest degrees.
'''

def supernode1(NUM_SEEDS, adj, deg_list):
    '''
    As module description says, but instead of picking all a node's
    neighbors, only pick as many as votes needed to remain our
    team's color.
    
    args:
    NUM_SEEDS, the number of seeds this graph requires
    adj, the graph adjacency list (raw JSON format)
    deg_list, a descending list of node ID's, sorted by their degree
    
    output:
    a list of NUM_SEEDS node ID's.
    '''
    output = []
    output.append(deg_list[NUM_SEEDS])
    for i in range(NUM_SEEDS):
        try:
            curr = output[i]
        except IndexError:
            break
        neighbors = adj[str(curr)]
        if len(neighbors) == 0:
            continue
        needed = int((len(adj[str(curr)]) + 1.5 + 1)/2)
        for j in range(min(needed, len(neighbors))):
            try:
                node = neighbors.pop()
            except IndexError:
                break
            if int(node) not in output:
                output.append(int(node))
    for x in deg_list[:NUM_SEEDS]:
        if x not in output:
            output.append(x)
    return output[:NUM_SEEDS]


def supernode2(NUM_SEEDS, adj, deg_list):
    '''
    As module description says.
    
    args:
    NUM_SEEDS, the number of seeds this graph requires
    adj, the graph adjacency list (raw JSON format)
    deg_list, a descending list of node ID's, sorted by their degree
    
    output:
    a list of NUM_SEEDS node ID's.
    '''
    output = []
    output.append(deg_list[NUM_SEEDS])
    for i in range(NUM_SEEDS):
        try:
            curr = output[i]
        except IndexError:
            break
        neighbors = adj[str(curr)]
        if len(neighbors) == 0:
            continue
        for node in neighbors:
            if int(node) not in output:
                output.append(int(node))
    for x in deg_list[:NUM_SEEDS]:
        if x not in output:
            output.append(x)
    return output[:NUM_SEEDS]