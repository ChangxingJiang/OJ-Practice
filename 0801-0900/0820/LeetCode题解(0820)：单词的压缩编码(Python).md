# LeetCode题解(0820)：单词的压缩编码(Python)

题目：[原题链接](https://leetcode-cn.com/problems/short-encoding-of-words/)（中等）

标签：字典树、哈希表

| 解法           | 时间复杂度     | 空间复杂度 | 执行用时      |
| -------------- | -------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(W×L+WlogW)$ | $O(W×L)$   | 96ms (86.49%) |
| Ans 2 (Python) |                |            |               |
| Ans 3 (Python) |                |            |               |

解法一：

```python
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x), reverse=True)

        ans = 0

        lst = set()
        for word in words:
            if word not in lst:
                ans += len(word) + 1
            for i in range(len(word)):
                lst.add(word[i:])

        return ans
```

