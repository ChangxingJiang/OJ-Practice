# LeetCode题解(1119)：删去字符串中的元音(Python)

题目：[原题链接](https://leetcode-cn.com/problems/remove-vowels-from-a-string/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms ( 79.64%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def removeVowels(self, S: str) -> str:
        vowels = {"a", "e", "i", "o", "u"}
        lst = []
        for ch in S:
            if ch not in vowels:
                lst.append(ch)
        return "".join(lst)
```