def supercluster1(NUM_SEEDS, adj, deg_list):
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


def supercluster2(NUM_SEEDS, adj, deg_list):
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