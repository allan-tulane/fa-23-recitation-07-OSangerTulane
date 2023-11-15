from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node]) 
    while len(frontier) != 0: 
        result_new = result | frontier 
        result = result_new  
        f = frontier.pop() 
        frontier_neighbors = graph[f] 
        frontier = frontier_neighbors - result 
    return result 



def connected(graph):
    Nodes = len(graph)
    connect = reachable(graph, list(graph.keys())[0])
    return len(connect) == Nodes


def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    result = []
    frontier = set(list(graph.keys()))
  
    while len(frontier) != 0:
      node = frontier.pop()
      connected = reachable(graph, node)
      frontier = frontier - connected
      result.append(connected)

    return len(result)

