# LeetCode题解(1817)：查找用户活跃分钟数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/finding-the-users-active-minutes/)（中等）

标签：哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 132ms (72.11%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        count = collections.defaultdict(set)

        for u, t in logs:
            count[u].add(t)

        ans = [0] * k

        for lst in count.values():
            v = len(lst)
            if v - 1 < k:
                ans[v - 1] += 1

        return ans
```

