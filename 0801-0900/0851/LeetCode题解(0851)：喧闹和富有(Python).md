# LeetCode题解(0851)：喧闹和富有(Python)

题目：[原题链接](https://leetcode-cn.com/problems/loud-and-rich/)（中等）

标签：图、拓扑排序、广度优先搜索、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 484ms (93.42%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)

        count = [0] * n  # 记录入度数量
        graph = [[] for _ in range(n)]  # 记录出度的图

        for x, y in richer:
            count[y] += 1
            graph[x].append(y)

        queue = collections.deque()
        for i, v in enumerate(count):
            if v == 0:
                queue.append(i)

        # 拓扑排序状态转移
        dp = [i for i in range(n)]
        while queue:
            i1 = queue.popleft()
            for i2 in graph[i1]:
                if quiet[dp[i1]] < quiet[dp[i2]]:
                    dp[i2] = dp[i1]
                count[i2] -= 1
                if count[i2] == 0:
                    queue.append(i2)

        return dp
```

