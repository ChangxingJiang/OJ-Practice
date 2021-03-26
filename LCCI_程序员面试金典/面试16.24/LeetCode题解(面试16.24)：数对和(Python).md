# LeetCode题解(面试16.24)：数对和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/pairs-with-sum-lcci/)（中等）

标签：哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 188ms (21.71%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        count = collections.Counter()
        for num in nums:
            another = target - num
            if count[another] > 0:
                count[another] -= 1
                ans.append([another, num])
            else:
                count[num] += 1

        return ans
```