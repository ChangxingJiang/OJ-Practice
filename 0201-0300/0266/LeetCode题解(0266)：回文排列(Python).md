# LeetCode题解(0266)：回文排列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/palindrome-permutation/)（简单）

标签：哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (55.79%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = set()
        for ch in s:
            if ch not in count:
                count.add(ch)
            else:
                count.remove(ch)
        return len(count) <= 1
```