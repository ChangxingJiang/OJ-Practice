# LeetCode题解(1400)：构造K个回文字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/construct-k-palindrome-strings/)（中等）

标签：贪心算法、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 128ms (35.40%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        count = set()
        for ch in s:
            if ch not in count:
                count.add(ch)
            else:
                count.remove(ch)

        return len(count) <= k
```

