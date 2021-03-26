# LeetCode题解(面试08.03)：魔术索引(Python)

题目：[原题链接](https://leetcode-cn.com/problems/magic-index-lcci/)（简单）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (97.45%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（直接查找）：

```python
class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if i == n:
                return i
        return -1
```

