import collections
from typing import List


class DSU:
    def __init__(self, n: int):
        self.array = [i for i in range(n)]
        self.size = [1] * n

    def find(self, i: int):
        if self.array[i] != i:
            self.array[i] = self.find(self.array[i])
        return self.array[i]

    def union(self, i: int, j: int):
        i = self.find(i)
        j = self.find(j)
        if self.size[i] >= self.size[j]:
            self.array[j] = i
            self.size[i] += self.size[j]
        else:
            self.array[i] = j
            self.size[j] += self.size[i]

    def arrange(self):
        for i in range(len(self.array)):
            self.find(i)


class Solution:
    class Node:
        def __init__(self):
            self.points = set()
            self.children = collections.Counter()
            self.father = 0

    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        s1, s2 = len(matrix), len(matrix[0])

        dsu = DSU(s1 * s2)

        # 统计每行中值相同的点
        # O(N×M)
        for i1 in range(s1):
            count = collections.defaultdict(list)
            for j1 in range(s2):
                count[matrix[i1][j1]].append(j1)
            for n in count:
                if len(count[n]) > 1:
                    lst = [i1 * s2 + j1 for j1 in count[n]]
                    for i in range(1, len(lst)):
                        dsu.union(lst[i - 1], lst[i])

        # 统计每列中值相同的点
        # O(N×M)
        for j1 in range(s2):
            count = collections.defaultdict(list)
            for i1 in range(s1):
                count[matrix[i1][j1]].append(i1)
            for n in count:
                if len(count[n]) > 1:
                    lst = [i1 * s2 + j1 for i1 in count[n]]
                    for i in range(1, len(lst)):
                        dsu.union(lst[i - 1], lst[i])

        # print("DSU:", dsu.array)

        # 构造有向图
        # O(N×M)
        queue = set()  # 拓扑排序的开头位置
        nodes = [[self.Node() for _ in range(s2)] for _ in range(s1)]  # 二维节点列表
        for i1 in range(s1):
            for j1 in range(s2):
                idx1 = i1 * s2 + j1
                idx2 = dsu.find(idx1)
                if idx2 == idx1:  # 当前节点位于并查集的根节点
                    nodes[i1][j1].points.add((i1, j1))
                    queue.add(nodes[i1][j1])
                else:  # 当前节点不在并查集的根节点
                    i2, j2 = divmod(idx2, s2)
                    nodes[i1][j1] = nodes[i2][j2]
                    nodes[i1][j1].points.add((i1, j1))
                    # print("DSU:", (i1, j1), "->", (i2, j2), ":", nodes[i1][j1].points)

        # 构造有向图中行的关系
        # O(M×N×log(N))
        for i1 in range(s1):
            count = collections.defaultdict(list)
            for j1 in range(s2):
                count[matrix[i1][j1]].append(j1)
            lst = list(sorted(count.keys()))
            for k in range(1, len(lst)):
                j2 = count[lst[k - 1]][0]  # 获取父节点（如果有多个父节点则它们已经被打包）
                j3 = count[lst[k]][0]  # 获取子节点（如果有多个子节点则它们已经被打包）
                nodes[i1][j2].children[nodes[i1][j3]] += 1
                nodes[i1][j3].father += 1
                if nodes[i1][j3] in queue:
                    queue.remove(nodes[i1][j3])

        # 构造有向图中列的关系
        # O(M×N×log(M))
        for j1 in range(s2):
            count = collections.defaultdict(list)
            for i1 in range(s1):
                count[matrix[i1][j1]].append(i1)
            lst = list(sorted(count.keys()))
            for k in range(1, len(lst)):
                i2 = count[lst[k - 1]][0]  # 获取父节点（如果有多个父节点则它们已经被打包）
                i3 = count[lst[k]][0]  # 获取子节点（如果有多个子节点则它们已经被打包）
                nodes[i2][j1].children[nodes[i3][j1]] += 1
                nodes[i3][j1].father += 1
                if nodes[i3][j1] in queue:
                    queue.remove(nodes[i3][j1])

        # 拓扑排序
        # O(N×M)
        ans = [[0] * s2 for _ in range(s1)]
        step = 1
        while queue:
            new_queue = set()
            for node1 in queue:
                for i1, j1 in node1.points:
                    ans[i1][j1] = step
                for node2, power in node1.children.items():
                    node2.father -= power
                    # print(node1.points, "->", node2.points, ":", node2.father)
                    if node2.father == 0:
                        new_queue.add(node2)
            queue = new_queue
            step += 1

        return ans


if __name__ == "__main__":
    # [[1,2],
    #  [2,3]]
    print(Solution().matrixRankTransform(matrix=[
        [1, 2],
        [3, 4]
    ]))

    # [[1,1],
    #  [1,1]]
    print(Solution().matrixRankTransform(matrix=[
        [7, 7],
        [7, 7]
    ]))

    # [[4,2,3],
    #  [1,3,4],
    #  [5,1,6],
    #  [1,3,4]]
    print(Solution().matrixRankTransform(matrix=[
        [20, -21, 14],
        [-19, 4, 19],
        [22, -47, 24],
        [-19, 4, 19]
    ]))

    # [[5,1,4],
    #  [1,2,3],
    #  [6,3,1]]
    print(Solution().matrixRankTransform(matrix=[
        [7, 3, 6],
        [1, 4, 5],
        [9, 8, 2]
    ]))

    # [[2,1,4,6],
    #  [2,6,5,4],
    #  [5,2,4,3],
    #  [4,3,1,5]]
    print(Solution().matrixRankTransform(matrix=[
        [-37, -50, -3, 44],
        [-37, 46, 13, -32],
        [47, -42, -3, -40],
        [-17, -22, -39, 24]
    ]))

    # [[7,13,1,5,4,6,9,8],
    #  [8,11,2,10,1,12,14,9],
    #  [2,14,1,11,13,7,5,3],
    #  [3,19,16,12,14,7,10,13],
    #  [8,12,6,14,5,1,4,13],
    #  [2,16,15,17,4,18,3,14],
    #  [3,7,11,6,12,13,14,10],
    #  [16,19,18,3,15,2,11,17]]
    print(Solution().matrixRankTransform(matrix=[
        [-23, 20, -49, -30, -39, -28, -5, -14],
        [-19, 4, -33, 2, -47, 28, 43, -6],
        [-47, 36, -49, 6, 17, -8, -21, -30],
        [-27, 44, 27, 10, 21, -8, 3, 14],
        [-19, 12, -25, 34, -27, -48, -37, 14],
        [-47, 40, 23, 46, -39, 48, -41, 18],
        [-27, -4, 7, -10, 9, 36, 43, 2],
        [37, 44, 43, -38, 29, -44, 19, 38]
    ]))
