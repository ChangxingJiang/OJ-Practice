# LeetCode题解(0041)：缺失的第一个正数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/first-missing-positive/)（困难）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 44ms (47.72%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（每个数最多被遍历三次）：

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i1 in range(size):
            n1 = i1 + 1
            while nums[i1] != n1:
                i2 = nums[i1] - 1
                if 0 <= i2 < size:
                    if nums[i1] != nums[i2]:
                        nums[i1], nums[i2] = nums[i2], nums[i1]
                    else:
                        nums[i2] = -1
                else:
                    nums[i1] = -1
                    break

        for i in range(size):
            if nums[i] == -1:
                return i + 1

        return size + 1
```