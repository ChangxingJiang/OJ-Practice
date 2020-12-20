# LeetCode题解(1180)：统计只含单一字母的子串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-substrings-with-only-one-distinct-letter/)（简单）

标签：字符串、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 32ms (98.44%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def countLetters(self, S: str) -> int:
        now = ""
        num = 0
        ans = 0
        for ch in S:
            if ch != now:
                ans += (1 + num) * num // 2
                now = ch
                num = 1
            else:
                num += 1
        ans += (1 + num) * num // 2
        return ans
```