# LeetCode题解(面试16.20)：T9键盘(Python)

题目：[原题链接](https://leetcode-cn.com/problems/t9-lcci/)（中等）

标签：数组、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(W)$     | $O(W)$     | 56ms (71.21%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        table = ["2", "2", "2", "3", "3", "3", "4", "4", "4", "5", "5", "5", "6", "6", "6", "7", "7", "7", "7", "8",
                 "8", "8", "9", "9", "9", "9"]

        size = len(num)

        ans = []
        for word in words:
            if len(word) != size:
                continue
            for i in range(len(word)):
                if table[ord(word[i])-97] != num[i]:
                    break
            else:
                ans.append(word)

        return ans
```