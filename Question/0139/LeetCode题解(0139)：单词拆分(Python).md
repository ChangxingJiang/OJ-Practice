# LeetCode题解(0139)：单词拆分(Python)

题目：[原题链接](https://leetcode-cn.com/problems/word-break/)（中等）

标签：动态规划、滑动窗口、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^3+D)$ | $O(D+N)$   | 36ms (97.32%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict:
            return False

        words = set(wordDict)
        max_length = max(len(word) for word in words)

        window = collections.deque([0])
        for i2 in range(1, len(s) + 1):
            if i2 - window[0] > max_length:
                window.popleft()
            if not window:
                return False
            for i1 in window:
                if s[i1:i2] in words:
                    window.append(i2)
                    break

        return window[-1] == len(s)
```

