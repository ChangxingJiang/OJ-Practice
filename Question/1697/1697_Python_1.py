import collections
from typing import List


def build_graph(edges):
    graph = collections.defaultdict(dict)
    for edge in edges:
        if edge[1] not in graph[edge[0]] or graph[edge[0]][edge[1]] > edge[2]:
            graph[edge[0]][edge[1]] = edge[2]
            graph[edge[1]][edge[0]] = edge[2]
    return graph


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # 构造图
        # O(E)
        graph = build_graph(edgeList)

        # Floyd_Warshall算法的传递闭包
        # O(N^2+NE)
        for k in range(n):
            for i in range(n):
                # 如果边(i,k)存在
                if i != k and k in graph[i]:
                    for j in range(n):
                        # 如果边(k,j)存在
                        if i != j != k and j in graph[k]:
                            distance = max(graph[i][k], graph[k][j])
                            if j not in graph[i] or graph[i][j] > distance:
                                graph[i][j] = distance

        ans = []
        for i, j, d in queries:
            ans.append(j in graph[i] and graph[i][j] < d)

        return ans


if __name__ == "__main__":
    # [False,True]
    print(Solution().distanceLimitedPathsExist(n=3, edgeList=[[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]],
                                               queries=[[0, 1, 2], [0, 2, 5]]))

    # [True,False]
    print(Solution().distanceLimitedPathsExist(n=5, edgeList=[[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]],
                                               queries=[[0, 4, 14], [1, 4, 13]]))
