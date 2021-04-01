# LeetCode题解(1805)：字符串中不同整数的数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-different-integers-in-a-string/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 48ms (22.66%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        ans = [""]
        for ch in word:
            if ch.isdigit():
                ans[-1] += ch
            else:
                ans.append("")
        return len({int(num) for num in ans if num != ""})
```

