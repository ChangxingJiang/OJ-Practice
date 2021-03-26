# LeetCode题解(1405)：最长快乐字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-happy-string/)（中等）

标签：贪心算法、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(A+B+C)$ | $O(1)$     | 24ms (100.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        a, b, c = min(a, 2 * (b + c + 1)), min(b, 2 * (a + c + 1)), min(c, 2 * (a + b + 1))

        ans = ["", ""]
        while a > 0 or b > 0 or c > 0:
            v1, v2, v3 = sorted([a, b, c], reverse=True)
            if v1 == a:
                if ans[-2] != "a" or ans[-1] != "a":
                    ans.append("a")
                    a -= 1
                else:
                    if v2 == b:
                        ans.append("b")
                        b -= 1
                    else:
                        ans.append("c")
                        c -= 1
            elif v1 == b:
                if ans[-2] != "b" or ans[-1] != "b":
                    ans.append("b")
                    b -= 1
                else:
                    if v2 == a:
                        ans.append("a")
                        a -= 1
                    else:
                        ans.append("c")
                        c -= 1
            else:
                if ans[-2] != "c" or ans[-1] != "c":
                    ans.append("c")
                    c -= 1
                else:
                    if v2 == a:
                        ans.append("a")
                        a -= 1
                    else:
                        ans.append("b")
                        b -= 1

        return "".join(ans)
```

