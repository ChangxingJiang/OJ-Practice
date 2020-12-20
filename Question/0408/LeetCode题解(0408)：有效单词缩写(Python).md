# LeetCode题解(0408)：有效单词缩写(Python)

题目：[原题链接](https://leetcode-cn.com/problems/valid-word-abbreviation/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 52ms (11.93%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        lst = []
        for ch in abbr:
            if ch.isnumeric() and lst and lst[-1].isnumeric():
                lst[-1] += ch
            else:
                lst.append(ch)

        i1, size = 0, len(word)
        for ch2 in lst:
            if ch2.isalpha():
                if i1 >= size or word[i1] != ch2:
                    return False
                i1 += 1
            else:
                if ch2[0] == "0":
                    return False
                i1 += int(ch2)

        return i1 == size
```