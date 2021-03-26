# LeetCode题解(1111)：有效括号的嵌套深度(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/)（中等）

标签：贪心算法、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 56ms (65.85%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = []
        level = 0
        for ch in seq:
            if ch == "(":
                ans.append(level % 2)
                level += 1
            else:
                level -= 1
                ans.append(level % 2)
        return ans
```

