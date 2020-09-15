import collections


# 生成图中边的集合表示
def build_graph_set(edges):
    import collections
    graph = collections.defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
    return graph
