# LeetCode题解(1732)：找到最高海拔(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-the-highest-altitude/)（简单）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时     |
| -------------- | ---------- | ---------- | ------------ |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 52ms (5.57%) |
| Ans 2 (Python) |            |            |              |
| Ans 3 (Python) |            |            |              |

解法一：

```python
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        now = 0
        for h in gain:
            now += h
            ans = max(ans, now)
        return ans
```

