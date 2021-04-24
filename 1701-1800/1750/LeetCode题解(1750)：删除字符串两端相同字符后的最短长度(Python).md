# LeetCode题解(1750)：删除字符串两端相同字符后的最短长度(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-length-of-string-after-deleting-similar-ends/)（中等）

标签：双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 116ms (41.91%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            new = left
            while new <= right and s[left] == s[new]:
                new += 1
            left = new

            new = right
            while new >= left and s[right] == s[new]:
                new -= 1
            right = new

        return right - left + 1
```

