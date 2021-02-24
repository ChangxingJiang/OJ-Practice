# LeetCode题解(1376)：通知所有员工所需的时间(Python)

题目：[原题链接](https://leetcode-cn.com/problems/time-needed-to-inform-all-employees/)（中等）

标签：深度优先搜索、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $(N)$      | 500ms (73.12%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(set)
        for i, m in enumerate(manager):
            graph[m].add(i)

        queue = collections.deque([(headID, 0)])
        ans = 0
        while queue:
            n1, t1 = queue.popleft()
            if graph[n1]:
                t2 = t1 + informTime[n1]
                ans = max(ans, t2)
                for n2 in graph[n1]:
                    queue.append((n2, t2))
        return ans
```

