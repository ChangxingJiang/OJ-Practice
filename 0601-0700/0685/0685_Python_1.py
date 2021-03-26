from typing import List


class DDSU:
    def __init__(self, n):
        self.array = [i for i in range(n)]

    def find(self, i):
        if self.array[i] != i:
            self.array[i] = self.find(self.array[i])
        return self.array[i]

    def union(self, i, j):
        self.array[self.find(j)] = self.find(i)


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DDSU(len(edges) + 1)  # 构造并查集实例
        candidates = []  # 候选结果
        parent = {}
        last = None
        for edge in edges:
            if edge[1] in parent:  # 当前目标节点已经有父节点
                candidates.append([parent[edge[1]], edge[1]])
                candidates.append([edge[0], edge[1]])
            else:
                parent[edge[1]] = edge[0]
                if dsu.find(edge[0]) == dsu.find(edge[1]):
                    last = edge
                else:
                    dsu.union(edge[0], edge[1])

        if not candidates:
            return last

        if dsu.find(candidates[1][0]) == dsu.find(candidates[1][1]):
            return candidates[1]
        else:
            return candidates[0]


if __name__ == "__main__":
    print(Solution().findRedundantDirectedConnection([[1, 2], [1, 3], [2, 3]]))  # [2,3]
    print(Solution().findRedundantDirectedConnection([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]))  # [4,1]
    print(Solution().findRedundantDirectedConnection([[2, 1], [3, 1], [4, 2], [1, 4]]))  # [2,1]
    print(Solution().findRedundantDirectedConnection([[3, 4], [4, 1], [1, 2], [2, 3], [5, 1]]))  # [4,1]
