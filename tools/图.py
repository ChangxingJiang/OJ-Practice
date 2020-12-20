import collections


# 生成无向图中边的邻接列表结构
def build_graph_set(edges):
    graph = collections.defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
    return graph


# 生成无向图加权中边的邻接列表结构
def build_graph_set_p(edges):
    graph = collections.defaultdict(dict)
    for edge in edges:
        graph[edge[0]][edge[1]] = edge[2]
        graph[edge[1]][edge[0]] = edge[2]
    return graph


# 生成有向图中边的邻接列表结构
# edge[0]->edge[1]的边;edge[1]->edge[0]的边
def build_graph(edges):
    graph_in = collections.defaultdict(set)
    graph_out = collections.defaultdict(set)
    for edge in edges:
        graph_in[edge[1]].add(edge[0])
        graph_out[edge[0]].add(edge[1])
    return graph_out, graph_in


# 生成有向加权图中边的邻接列表结构
def build_graph_set_d_p(edges):
    graph = collections.defaultdict(dict)
    for edge in edges:
        graph[edge[0]][edge[1]] = edge[2]
    return graph


# 拓扑排序
def topo(graph_in, graph_out):
    count = {}  # 节点入射边统计
    queue = []  # 当前入射边为0的节点列表

    # 统计所有节点的入射边
    for node in graph_in:
        count[node] = len(graph_in[node])
    for node in graph_out:
        if node not in count:
            count[node] = 0
            queue.append(node)

    # 拓扑排序
    order = []
    while queue:
        node = queue.pop()
        order.append(node)
        for next in graph_out[node]:
            count[next] -= 1
            if count[next] == 0:
                queue.append(next)

    return order
