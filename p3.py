def aStarAlgo(start_node, stop_node):
    open_set = set(start_node)
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}
    
    while len(open_set) > 0:
        n = min(open_set, key=lambda node: g[node] + heuristic(node))
        
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            return path
        
        open_set.remove(n)
        closed_set.add(n)
        
        if n in Graph_nodes:
            for (m, weight) in Graph_nodes[n]:
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                elif g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)
    
    return None

def heuristic(n):
    H_dist = {'A': 11, 'B': 6, 'C': 99, 'D': 1, 'E': 7, 'G': 0}
    return H_dist[n]

Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
}

path = aStarAlgo('A', 'G')
if path is None:
    print('Path does not exist!')
else:
    print('Path found:', path)
