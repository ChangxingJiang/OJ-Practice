from typing import List


class DSU:
    def __init__(self, n: int):
        self.array = [i for i in range(n)]
        self.size = [1] * n

    def find(self, i: int):
        """查询i所属的连通分支"""
        if self.array[i] != i:
            self.array[i] = self.find(self.array[i])
        return self.array[i]

    def union(self, i: int, j: int):
        """合并i和j的连通分支"""
        i = self.find(i)
        j = self.find(j)
        if self.size[i] >= self.size[j]:
            self.array[j] = i
            self.size[i] += self.size[j]
        else:
            self.array[i] = j
            self.size[j] += self.size[i]

    def group_num(self):
        """计算当前的连通分支数量"""
        group = set()
        for i in range(len(self.array)):
            if self.array[i] not in group and self.find(i) not in group:
                group.add(self.find(i))
        return len(group)

    def __repr__(self):
        return str(len(self.array)) + ":" + str(self.array)


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # 将边依据不同的情况排序
        edges1, edges2, edges3 = [], [], []
        for edge in edges:
            if edge[0] == 1:
                edges1.append((edge[1] - 1, edge[2] - 1))
            elif edge[0] == 2:
                edges2.append((edge[1] - 1, edge[2] - 1))
            else:  # edge[0] == 3
                edges3.append((edge[1] - 1, edge[2] - 1))

        dsu1 = DSU(n)
        dsu2 = DSU(n)

        ans = 0  # 被移除的边的数量

        # 遍历第3类的边
        for t, n1, n2 in edges:
            if dsu1.find(n1) == dsu1.find(n2):  # 如果两条端点已经被连通，则移除当前边
                ans += 1
            else:  # 如果两个端点没有被连通，则保留当前边
                dsu1.union(n1, n2)
                dsu2.union(n1, n2)

        # 遍历第1类的边
        for n1, n2 in edges1:
            if dsu1.find(n1) == dsu1.find(n2):
                ans += 1
            else:
                dsu1.union(n1, n2)

        # 遍历第2类的边
        for n1, n2 in edges2:
            if dsu2.find(n1) == dsu2.find(n2):
                ans += 1
            else:
                dsu2.union(n1, n2)

        # 检查是否可以连通所有边
        return ans if (dsu1.group_num() == 1 and dsu2.group_num() == 1) else -1


if __name__ == "__main__":
    # 2
    print(Solution().maxNumEdgesToRemove(n=4, edges=[[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]))

    # 0
    print(Solution().maxNumEdgesToRemove(n=4, edges=[[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]))

    # -1
    print(Solution().maxNumEdgesToRemove(n=4, edges=[[3, 2, 3], [1, 1, 2], [2, 3, 4]]))

    # 0
    print(Solution().maxNumEdgesToRemove(n=4, edges=[[3, 1, 2], [3, 3, 4], [1, 1, 3], [2, 2, 4]]))
