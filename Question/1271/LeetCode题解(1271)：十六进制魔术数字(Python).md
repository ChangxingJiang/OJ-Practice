# LeetCode题解(1271)：十六进制魔术数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/hexspeak/)（简单）

标签：数学、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(logN)$  | 44ms (21.15%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def toHexspeak(self, num: str) -> str:
        res = hex(int(num))[2:].upper().replace("0", "O").replace("1", "I")
        return res if res.isalpha() else "ERROR"
```