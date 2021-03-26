# LeetCode题解(0918)：环形子数组的最大和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-sum-circular-subarray/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 228ms (58.44%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        ans1 = cur1 = 0
        for n in A:
            cur1 = n + max(cur1, 0)
            ans1 = max(ans1, cur1)

        if ans1 == 0:
            res = max(A)
            return res

        # 如果在循环数组中，一定包含首尾，那么用总和减去首尾最小值即可
        ans2 = cur2 = 0
        for n in A:
            cur2 = n + min(cur2, 0)
            ans2 = min(ans2, cur2)

        return max(ans1, sum(A) - ans2)
```

