# LeetCode题解(面试01.04)：判断字符串是否为可转换为回文排列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/palindrome-permutation-lcci/)（简单）

标签：字符串、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (67.47%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        lst = set()
        for ch in s:
            if ch not in lst:
                lst.add(ch)
            else:
                lst.remove(ch)
        return len(lst) <= 1
```

