# LeetCode题解(1819)：序列中不同最大公约数的数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-different-subsequences-gcds/)（困难）

标签：数学

| 解法           | 时间复杂度   | 空间复杂度 | 执行用时        |
| -------------- | ------------ | ---------- | --------------- |
| Ans 1 (Python) | $O(N+ClogC)$ | $O(C)$     | 3052ms (82.32%) |
| Ans 2 (Python) |              |            |                 |
| Ans 3 (Python) |              |            |                 |

解法一：

```python
import math


class Solution:
    _MAXIMUM = 2 * (10 ** 5)

    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        nums = set(nums)
        m = max(nums)

        ans = 0

        for i in range(1, m + 1):
            if i in nums:
                ans += 1
                continue
                
            gcd = 0
            for j in range(i, m + 1, i):
                if j in nums:
                    if not gcd:
                        gcd = j
                    else:
                        gcd = math.gcd(gcd, j)
                    if gcd == i:
                        ans += 1
                        break

        return ans
```

