# LeetCode题解(0078)：计算无重复数组的所有子集(Python)

题目：[原题链接](https://leetcode-cn.com/problems/subsets/)（中等）

标签：回溯算法、数组、位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(2^N)$   | $O(1)$     | 40ms (73.72%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(2 ** len(nums)):
            now = []
            idx = len(nums) - 1
            while i:
                if i & 1:
                    now.append(nums[idx])
                idx -= 1
                i >>= 1
            ans.append(now)

        return ans
```