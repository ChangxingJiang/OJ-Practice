# LeetCode题解(1165)：单行键盘(Python)

题目：[原题链接](https://leetcode-cn.com/problems/single-row-keyboard/)（简单）

标签：字符串、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(K+W)$   | $O(K)$     | 52ms (90.22%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        dic = {ch: i for i, ch in enumerate(keyboard)}
        ans = 0
        now = 0
        for ch in word:
            ans += abs(dic[ch] - now)
            now = dic[ch]
        return ans
```