# LeetCode题解(0802)：找到最终的安全状态(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-eventual-safe-states/)（中等）

标签：图、拓扑排序、广度优先搜索、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N+E)$   | $O(N+E)$   | 180ms (53.74%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def eventualSafeNodes(self, graph1: List[List[int]]) -> List[int]:
        size = len(graph1)

        ans = []

        count = collections.Counter()
        queue = collections.deque()
        graph2 = [[] for _ in range(size)]  # 入度图
        for i in range(size):
            count[i] = len(graph1[i])
            for j in graph1[i]:
                graph2[j].append(i)
            if count[i] == 0:
                queue.append(i)
                ans.append(i)

        while queue:
            i1 = queue.popleft()
            for i2 in graph2[i1]:
                count[i2] -= 1
                if count[i2] == 0:
                    queue.append(i2)
                    ans.append(i2)

        ans.sort()
        return ans
```

