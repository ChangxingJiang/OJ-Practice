# LeetCode题解(0524)：通过删除字母匹配到字典里最长单词(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/)（中等）

标签：排序、双指针

| 解法           | 时间复杂度    | 空间复杂度 | 执行用时       |
| -------------- | ------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN+NS)$ | $O(logN)$  | 632ms (39.11%) |
| Ans 2 (Python) |               |            |                |
| Ans 3 (Python) |               |            |                |

解法一：

```python
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (-len(x), x))
        for word in d:
            i1 = i2 = 0
            while i1 < len(word) and i2 < len(s):
                if s[i2] == word[i1]:
                    i1 += 1
                    i2 += 1
                else:
                    i2 += 1
            if i1 == len(word):
                return word
        return ""
```

