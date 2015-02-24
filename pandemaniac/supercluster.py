NUM_SEEDS = 20

def supercluster1(adj, deg_list):
    output = []
    output.append(deg_list[NUM_SEEDS])
    for i in range(NUM_SEEDS):
        curr = output[i]
        # get current node's neighbors
        neighbors = adj[str(curr)]
        # votes needed if all nodes surrounding are colored (=total votes/2 rounded up)
        needed = int((len(adj[str(curr)]) + 1.5 + 1)/2)
        

def supercluster2(adj, deg_list):
    '''Currently defaults to picking the top NUM_SEEDS highest degree
    nodes.'''
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