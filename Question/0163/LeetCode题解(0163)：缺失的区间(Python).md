# LeetCode题解(0163)：缺失的区间(Python)

题目：[原题链接](https://leetcode-cn.com/problems/missing-ranges/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 24ms (100.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = []

        nums.append(upper + 1)
        now = lower - 1
        for n in nums:
            if n - now == 2:
                ans.append(str(n - 1))
            elif n - now > 2:
                ans.append(str(now + 1) + "->" + str(n - 1))
            now = n

        return ans
```