# LeetCode题解(1408)：寻找单词数组中是其他单词子串的单词(Python)

题目：[原题链接](https://leetcode-cn.com/problems/string-matching-in-an-array/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(1)$     | 40ms (91.37%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（暴力解法）：

```python
def stringMatching(self, words: List[str]) -> List[str]:
    ans = []
    for i1 in range(len(words)):
        word1 = words[i1]
        for i2 in range(len(words)):
            word2 = words[i2]
            if i1 != i2 and word1 in word2:
                ans.append(word1)
                break
    return ans
```