import collections
from itertools import combinations
from typing import List


def build_graph_set(edges):
    graph = collections.defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
    return graph


class DSU:
    def __init__(self, n):
        self.array = [i for i in range(n)]
        self.size = [1] * n

    def find(self, i):
        if self.array[i] != i:
            self.array[i] = self.find(self.array[i])
        return self.array[i]

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if self.size[i] >= self.size[j]:
            self.array[j] = i
            self.size[i] += self.size[j]
        else:
            self.array[i] = j
            self.size[j] += self.size[i]


class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        # 初始化距离列表
        D = [[float("inf")] * n for _ in range(n)]

        for i in range(n):
            D[i][i] = 0

        # 初始化填写距离列表
        for edge in edges:
            D[edge[0] - 1][edge[1] - 1] = 1
            D[edge[1] - 1][edge[0] - 1] = 1

        # 计算其他距离
        for node1 in range(n):
            now_level = collections.deque([node2 for node2, distance in enumerate(D[node1]) if distance == 1])
            while now_level:
                node2 = now_level.popleft()
                for node3, distance in enumerate(D[node2]):
                    if D[node1][node2] + distance < D[node1][node3]:
                        D[node1][node3] = D[node1][node2] + distance
                        now_level.append(node3)

        # for line in D:
        #     print(line)

        # 计算最终答案
        ans = [0] * n

        for value in range(2, n + 1):
            for group in list(combinations([s for s in range(n)], value)):
                max_distance = 0
                dsu = DSU(value)
                for i in range(value):
                    for j in range(i + 1, value):
                        if D[group[i]][group[j]] == 1:
                            dsu.union(i, j)
                        max_distance = max(max_distance, D[group[i]][group[j]])
                for i in range(value):
                    dsu.find(i)
                if len(set(dsu.array)) == 1:
                    ans[max_distance] += 1
                # print(group, ":", dsu.array, max_distance)

        return ans[1:]


if __name__ == "__main__":
    # print(Solution().countSubgraphsForEachDiameter(n=4, edges=[[1, 2], [2, 3], [2, 4]]))  # [3,4,0]
    # print(Solution().countSubgraphsForEachDiameter(n=2, edges=[[1, 2]]))  # [1]
    # print(Solution().countSubgraphsForEachDiameter(n=3, edges=[[1, 2], [2, 3]]))  # [2,1]
    print(Solution().countSubgraphsForEachDiameter(n=5, edges=[[1, 5], [2, 3], [2, 4], [2, 5]]))  # [4,5,3,0]
