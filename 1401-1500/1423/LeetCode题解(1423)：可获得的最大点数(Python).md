# LeetCode题解(1423)：可获得的最大点数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards/)（中等）

标签：数组、双指针、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 124ms (26.36%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints)

        window = size - k
        now = sum(cardPoints[:window])

        ans = now
        for i in range(window, size):
            now += cardPoints[i] - cardPoints[i - window]
            ans = min(ans,now)
        return sum(cardPoints) - ans
```

