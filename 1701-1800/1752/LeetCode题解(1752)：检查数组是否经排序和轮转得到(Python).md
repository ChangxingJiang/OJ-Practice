# LeetCode题解(1752)：检查数组是否经排序和轮转得到(Python)

题目：[原题链接](https://leetcode-cn.com/problems/check-if-array-is-sorted-and-rotated/)（简单）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 32ms (95.91%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def check(self, nums: List[int]) -> bool:
        find = False
        for i in range(len(nums)):
            if nums[i - 1] > nums[i]:
                if not find:
                    find = True
                else:
                    return False
        return True
```

