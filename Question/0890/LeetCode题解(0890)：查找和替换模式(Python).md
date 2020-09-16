# LeetCode题解(0890)：字符串的模式查找(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-and-replace-pattern/)（中等）

标签：字符串、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (87.42%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            if len(word) != len(pattern):
                continue
            mapping = {}
            values = set()
            for i in range(len(word)):
                if word[i] not in mapping:
                    if pattern[i] in values:
                        break
                    else:
                        mapping[word[i]] = pattern[i]
                        values.add(pattern[i])
                elif mapping[word[i]] != pattern[i]:
                    break
            else:
                ans.append(word)
        return ans
```