# LeetCode题解(1641)：统计字典序元音字符串的数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-sorted-vowel-strings/)（中等）

标签：数学、动态规划、记忆化递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时 |
| -------------- | ---------- | ---------- | -------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms     |
| Ans 2 (Python) |            |            |          |
| Ans 3 (Python) |            |            |          |

解法一：

```python
class Solution:
    @functools.lru_cache(None)
    def countVowelStrings(self, n: int, t=5) -> int:
        if t == 0:
            return 0
        if n == 1:
            return t

        ans = 0
        for i in range(1, t + 1):
            ans += self.countVowelStrings(n - 1, i)
        return ans
```