# LeetCode题解(0293)：翻转游戏(Python)

题目：[原题链接](https://leetcode-cn.com/problems/flip-game/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (84.13%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        ans = []
        for i in range(len(s) - 1):
            if s[i:i + 2] == "++":
                ans.append(s[:i] + "--" + s[i + 2:])
        return ans
```