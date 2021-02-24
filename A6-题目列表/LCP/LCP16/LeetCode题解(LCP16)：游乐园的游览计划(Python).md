# LeetCode题解(LCP16)：游乐园的游览计划(Python)

题目：[原题链接](https://leetcode-cn.com/problems/you-le-yuan-de-you-lan-ji-hua/)（困难）

标签：

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时     |
| -------------- | ---------- | ---------- | ------------ |
| Ans 1 (Python) | $O(N^3)$   | $O(N+E)$   | 超出时间限制 |
| Ans 2 (Python) |            |            |              |
| Ans 3 (Python) |            |            |              |

解法一：

```python
class Solution:
    def maxWeight(self, edges: List[List[int]], value: List[int]) -> int:
        n = len(value)

        # 构造图
        graph = collections.defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        ans = 0

        # 遍历每个景点为重点景点A
        for a in range(n):
            # 计算所有可能的路径
            near = graph[a]
            path = []
            for j in near:
                for k in near:
                    if j < k and k in graph[j]:  # j < k -> 确保每条路径只被添加一次
                        path.append([j, k])

            # 计算最大的路径组合
            if len(path) == 0:
                continue
            elif len(path) == 1:
                b, c = path[0][0], path[0][1]
                ans = max(ans, value[a] + value[b] + value[c])
            else:
                for j1 in range(len(path)):
                    for j2 in range(j1 + 1, len(path)):
                        res = value[a]
                        for j in {path[j1][0], path[j1][1], path[j2][0], path[j2][1]}:
                            res += value[j]
                        ans = max(ans, res)

        return ans
```

