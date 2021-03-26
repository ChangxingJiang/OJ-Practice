# LeetCode题解(0978)：最长湍流子数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-turbulent-subarray/)（中等）

标签：数组、贪心算法、动态规划、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 216ms (62.45%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = 0
        now = []
        for n in arr:
            if len(now) == 0:
                now.append(n)
                ans = max(ans, len(now))
            elif len(now) == 1:
                if now[-1] != n:
                    now.append(n)
                    ans = max(ans, len(now))
                else:
                    pass
            elif len(now) == 2 and (now[-1] - now[-2]) * (n - now[-1]) > 0:
                now = [now[-1], n]
            elif (now[-1] - now[-2]) * (n - now[-1]) < 0:
                now.append(n)
                ans = max(ans, len(now))
            else:
                now = [now[-1], n]
        return ans
```

