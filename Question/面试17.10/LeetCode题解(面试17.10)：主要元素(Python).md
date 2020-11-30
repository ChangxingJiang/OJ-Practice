# LeetCode题解(面试17.10)：主要元素(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-majority-element-lcci/)（简单）

标签：数学、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 52ms (67.71%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major, count = -1, 0
        for n in nums:
            if count == 0:
                major = n
                count += 1
            elif major == n:
                count += 1
            else:
                count -= 1

        count = 0
        for n in nums:
            if major == n:
                count += 1

        return major if count > len(nums) // 2 else -1
```