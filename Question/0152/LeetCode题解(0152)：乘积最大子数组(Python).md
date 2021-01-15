# LeetCode题解(0152)：乘积最大子数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-product-subarray/)（中等）

标签：贪心算法、数组、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 60ms (17.95%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float("-inf")
        last1 = 0  # 绝对值最大的正数
        last2 = 0  # 绝对值最大的负数
        for num in nums:
            if num == 0:
                last1, last2 = 0, 0
                ans = max(ans, 0)
            elif num > 0:
                last1, last2 = ((last1 * num) if last1 != 0 else num), ((last2 * num) if last2 != 0 else 0)
                ans = max(ans, last1)
            else:
                last1, last2 = ((last2 * num) if last2 != 0 else 0), ((last1 * num) if last1 != 0 else num)
                ans = max(ans, last2, last1 if last1 != 0 else float("-inf"))

        return ans
```

