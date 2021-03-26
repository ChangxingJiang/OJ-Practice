# LeetCode题解(1665)：完成所有任务的最少初始能量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-initial-energy-to-finish-tasks/)（困难）

标签：贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 268ms (53.49%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # 计算总消耗
        # O(N)
        ans = sum(task[0] for task in tasks)

        # 计算当前最大剩余量
        # O(N)
        # now = min(task[1] - task[0] for task in tasks)

        # 缩减剩余量
        # O(NlogN)
        surplus = [(task[1] - task[0], task[1]) for task in tasks]
        surplus.sort()

        # print(surplus)

        now = 0
        # now = surplus[]
        for s1, s2 in surplus:
            # print(now, s1, s2, "->", s1 - now if s1 > now else 0, "->", ans)
            if s1 > now:
                ans += s1 - now
                now = s1
            now += (s2 - s1)

        return ans
```

