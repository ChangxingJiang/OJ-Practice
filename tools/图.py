import collections


# 生成无向图中边的集合表示
def build_graph_set(edges):
    graph = collections.defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
    return graph


# 生成无向图加权中边的集合表示
def build_graph_set_p(edges):
    graph = collections.defaultdict(dict)
    for edge in edges:
        graph[edge[0]][edge[1]] = edge[2]
        graph[edge[1]][edge[0]] = edge[2]
    return graph


# 生成有向图中边的集合表示
def build_graph_set_d(edges):
    graph = collections.defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge[1])
    return graph


# 生成有向加权图中边的集合表示
def build_graph_set_d_p(edges):
    graph = collections.defaultdict(dict)
    for edge in edges:
        graph[edge[0]][edge[1]] = edge[2]
    return graph
