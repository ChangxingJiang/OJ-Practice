# LeetCode题解(0761)：特殊的二进制序列交换后的最大值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/special-binary-string/)（困难）

标签：字符串、双指针、递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^3)$   | $O(N)$     | 44ms (64.29%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        if not S:
            return ""

        lst = []

        num = 0
        pos = 0
        for i, ch in enumerate(S):
            if ch == "1":
                num += 1
            else:
                num -= 1
            if num == 0:
                lst.append("1" + self.makeLargestSpecial(S[pos + 1:i]) + "0")
                pos = i + 1

        return "".join(sorted(lst, reverse=True))
```

