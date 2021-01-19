# LeetCode题解(0984)：不含AAA或BBB的字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/string-without-aaa-or-bbb/)（中等）

标签：贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时     |
| -------------- | ---------- | ---------- | ------------ |
| Ans 1 (Python) | $O(A+B)$   | $O(1)$     | 56ms (5.29%) |
| Ans 2 (Python) |            |            |              |
| Ans 3 (Python) |            |            |              |

解法一：

```python
class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        ans = []
        while A or B:
            if len(ans) >= 2 and ans[-2] == ans[-1]:
                if ans[-1] == "a":
                    ans.append("b")
                    B -= 1
                else:
                    ans.append("a")
                    A -= 1
            elif A > B:
                ans.append("a")
                A -= 1
            else:
                ans.append("b")
                B -= 1

        return "".join(ans)
```

