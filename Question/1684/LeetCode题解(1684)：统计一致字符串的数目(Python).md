# LeetCode题解(1684)：统计一致字符串的数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-the-number-of-consistent-strings/)（简单）

标签：哈希表、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N+W×L)$ | $O(N)$     | 96ms (67.45%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        allowed = set(allowed)
        for word in words:
            word = set(word)
            if word <= allowed:
                ans += 1
        return ans
```

