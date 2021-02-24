# LeetCode题解(1395)：统计作战单位数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-number-of-teams/)（中等）

标签：数组、线段树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(1)$     | 1156ms (19.28%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        size = len(rating)

        ans = 0

        for j in range(1, size - 1):
            n1 = n2 = n3 = n4 = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    n1 += 1
                elif rating[i] > rating[j]:
                    n3 += 1
            for k in range(j + 1, size):
                if rating[j] < rating[k]:
                    n2 += 1
                elif rating[j] > rating[k]:
                    n4 += 1
            ans += n1 * n2 + n3 * n4

        return ans
```

