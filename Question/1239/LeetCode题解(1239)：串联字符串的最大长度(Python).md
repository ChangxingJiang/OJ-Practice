# LeetCode题解(1239)：串联字符串的最大长度(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/)（中等）

标签：回溯算法、位运算、递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(2^N)$   | $O(2^N)$   | 76ms (93.94%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = [s for s in arr if len(s) == len(set(s))]

        stats = []
        for word in arr:
            stat = 0
            for ch in word:
                stat |= 1 << (ord(ch) - 97)
            stats.append(stat)

        def dfs(i, s, x):
            if i == len(arr):
                return x
            res = dfs(i + 1, s, x)
            if not s & stats[i]:
                res = max(res, dfs(i + 1, s | stats[i], x + len(arr[i])))
            return res

        return dfs(0, 0, 0)
```

