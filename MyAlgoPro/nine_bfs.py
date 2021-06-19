# O(n + m) time - where n is # of node, m is # of edge
# O(n) space
def bfs(start_node):
    # Must use queue in BFS, not stack.
    # distance(dict): 
    # 1. Get record of node in queue to avoid requesting again.
    # 2. Get record of the min distance from start_node to other nodes.
    queue = collections.deque([start_node])
    distance = {start_node: 0}

    # while the queue is not empty, keep fetching node from queue 
    # to expand neighbor to queue.
    while queue:
        node = queue.popleft()

        # If there is terminating condition.
        if node is A: # A is the terminating condition
            break # or return something

        for neighbor in node.get_neighbors():
            if neighbor in distance:
                continue
            queue.append(neighbor)
            distance[neighbor] = distance[node] + 1    

    # Need the distance from all nodes to start_node, return hashmap
    return distance

    # Need the connected nodes, return all nodes in hashmap
    return distance.keys()

    # Need the min distance from end_node
    return distance[end_node]



## topological sorting
def get_indegrees(nodes):
    counter = {node: 0 for node in nodes}
    for node in nodes:
        for neighbor in node.get_neighbors():
            counter[neighbor] += 1
    return counter

def topological_sort(nodes):
    # Calculate indegrees
    indegrees = get_indegrees(nodes)

    # Put 0 indegree node to queue
    queue = collections.deque([
        node
        for node in nodes
        if indegrees[node] == 0
    ])

    # Use BFS get node from graph
    topo_order = []
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in node.get_neighbors():
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)

    #
    if len(topo_order) != len(nodes):
        return # Circle(loop depend), no topo order
    return topo_order                 