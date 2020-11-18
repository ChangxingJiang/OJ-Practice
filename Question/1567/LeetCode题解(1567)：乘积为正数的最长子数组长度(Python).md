# LeetCode题解(1567)：计算乘积为正数的最长子数组的长度(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-length-of-subarray-with-positive-product/)（中等）

标签：贪心算法、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 228ms (49%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一（正反向分别查找）：

```python
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = 0

        # 正向查找
        now = 0
        temp = 1
        last = 0
        for num in nums:
            if num > 0:
                if temp > 0:
                    now += 1
                    last += 1
                    ans = max(ans, now)
                else:
                    last += 1
            elif num < 0:
                if temp > 0:
                    last += 1
                else:
                    last += 1
                    now = last
                    ans = max(ans, now)
                temp *= -1
            else:
                now = 0
                last = 0
                temp = 1

        # 反向查找
        now = 0
        temp = 1
        last = 0
        for num in nums[::-1]:
            if num > 0:
                if temp > 0:
                    now += 1
                    last += 1
                    ans = max(ans, now)
                else:
                    last += 1
            elif num < 0:
                if temp > 0:
                    last += 1
                else:
                    last += 1
                    now = last
                    ans = max(ans, now)
                temp *= -1
            else:
                now = 0
                last = 0
                temp = 1

        return ans
```