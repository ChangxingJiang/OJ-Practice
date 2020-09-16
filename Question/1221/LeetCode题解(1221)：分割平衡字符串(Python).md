# LeetCode题解(1221)：L和R数量相同的平衡字符串可以分隔为多少个子平衡字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/split-a-string-in-balanced-strings/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 32ms (96.76%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num = 0
        ans = 0
        for c in s:
            if c == "L":
                num -= 1
            elif c == "R":
                num += 1
            if num == 0:
                ans += 1
        return ans
```

