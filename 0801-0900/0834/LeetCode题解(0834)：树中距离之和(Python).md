# LeetCode题解(0834)：树中每个节点到其他所有节点的距离之和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sum-of-distances-in-tree/)（困难）

标签：树、图、图-无向图、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 432ms (41.49%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 424ms (50.00%) |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        count = [1] * N  # 子树计数项
        ans = [0] * N  # 子树距离计数项

        # 深度优先搜索统计子树数量
        def dfs_count_sub(node, parent=None):
            for child in graph[node]:
                if child != parent:
                    dfs_count_sub(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child]
            ans[node] += count[node] - 1

        # 统计子树数量
        dfs_count_sub(0)

        # 深度优先搜索计算最终结果
        def dfs_count_ans(node, parent=-1):
            if parent != -1:
                parent_num = N - count[node] - 1
                node_num = count[node] - 1
                ans[node] = ans[parent] - node_num + parent_num
                # print(node, ":", ans[parent], "-", node_num, "+", parent_num, "->", ans[node])
            for child in graph[node]:
                if child != parent:
                    dfs_count_ans(child, node)

        # 计算最终结果
        dfs_count_ans(0)
        return ans
```

解法二（优化解法一）：

```python
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        count = [1] * N  # 子树计数项
        depth = [0] * N  # 节点深度（用于计算当前根节点的结果）

        # 深度优先搜索统计子树数量
        def dfs_count_sub(node, parent=None):
            for child in graph[node]:
                if child != parent:
                    depth[child] += depth[node] + 1
                    dfs_count_sub(child, node)
                    count[node] += count[child]

        # 统计子树数量
        ans = [0] * N  # 子树距离计数项
        dfs_count_sub(0)
        ans[0] = sum(depth)

        # 深度优先搜索计算最终结果
        def dfs_count_ans(node, parent=-1):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] + N - 2 * count[child]
                    dfs_count_ans(child, node)

        # 计算最终结果
        dfs_count_ans(0)
        return ans
```