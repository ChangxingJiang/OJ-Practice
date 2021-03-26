# LeetCode题解(1652)：拆炸弹(Python)

题目：[原题链接](https://leetcode-cn.com/problems/defuse-the-bomb/)（简单）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 52ms (44.78%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        elif k > 0:
            res = []
            for i in range(len(code)):
                val = 0
                for j in range(i + 1, i + k + 1):
                    j %= len(code)
                    val += code[j]
                res.append(val)
            return res
        else:
            res = []
            for i in range(len(code)):
                val = 0
                for j in range(i + k, i):
                    j = (j + len(code)) % len(code)
                    val += code[j]
                res.append(val)
            return res
```