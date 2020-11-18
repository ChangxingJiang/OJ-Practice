# LeetCode题解(1624)：两个相同字符之间的最长子字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/largest-substring-between-two-equal-characters/)（简单）

标签：字符串、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (76%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        dic = {}
        for i, ch in enumerate(s):
            if ch in dic:
                ans = max(ans, i - dic[ch] - 1)
            else:
                dic[ch] = i
        return ans
```