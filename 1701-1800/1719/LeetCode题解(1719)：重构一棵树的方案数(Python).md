# LeetCode题解(1719)：重构一棵树的方案数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-ways-to-reconstruct-a-tree/)（困难）

标签：分治算法、图、深度优先搜索、树、递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 2456ms (31.82%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def __init__(self):
        self.graph = collections.defaultdict(set)

    def checkWays(self, pairs: List[List[int]]) -> int:
        # 构造图结构和节点列表
        nodes = set()
        for n1, n2 in pairs:
            nodes.add(n1)
            nodes.add(n2)
            self.graph[n1].add(n2)
            self.graph[n2].add(n1)

        # 深度优先搜索：不断移除根节点并递归它的所有子树
        return self.dfs(nodes)

    def dfs(self, nodes):
        # 寻找根节点
        roots = []
        for n1 in nodes:
            num = 0
            for n2 in self.graph[n1]:
                if n2 in nodes:
                    num += 1
            if num == len(nodes) - 1:
                roots.append(n1)

        # 如果没有根节点，则没有结果
        if len(roots) == 0:
            return 0

        # 如果已经有多个根则标记（用于返回2）
        maybe = 1
        if len(roots) > 1:
            maybe = 2

        # 移除所有可能的根节点（所有可能的根节点可以排成形如测试用例2的一竖列的情形）
        for n in roots:
            nodes.remove(n)

        # 遍历所有的连通分支
        while nodes:
            queue = collections.deque([nodes.pop()])
            sub_nodes = set()
            while queue:
                n1 = queue.popleft()
                sub_nodes.add(n1)
                for n2 in self.graph[n1]:
                    if n2 in nodes:
                        nodes.remove(n2)
                        queue.append(n2)

            # 递归处理当前连通分支子树
            res = self.dfs(sub_nodes)

            if res == 0:
                return 0
            if res == 2:
                maybe = 2

        return maybe
```

