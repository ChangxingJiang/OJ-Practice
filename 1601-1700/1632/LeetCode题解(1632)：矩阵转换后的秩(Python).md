# LeetCode题解(1632)：矩阵转换后的秩(Python)

题目：[原题链接](https://leetcode-cn.com/problems/rank-transform-of-a-matrix/)（困难）

标签：并查集、拓扑排序、贪心算法

| 解法           | 时间复杂度       | 空间复杂度 | 执行用时       |
| -------------- | ---------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N×M×log(NM))$ | $O(N×M)$   | 4740ms (7.18%) |
| Ans 2 (Python) |                  |            |                |
| Ans 3 (Python) |                  |            |                |

解法一：

```python
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
```

