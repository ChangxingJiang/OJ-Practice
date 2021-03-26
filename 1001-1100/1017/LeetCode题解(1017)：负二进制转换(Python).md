# LeetCode题解(1017)：负二进制转换(Python)

题目：[原题链接](https://leetcode-cn.com/problems/convert-to-base-2/)（中等）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 36ms (77.33%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def baseNeg2(self, N: int) -> str:
        now = 1
        ans = []
        while N:
            if now > 0:
                if N & (-N) == now:
                    N -= now
                    ans.append("1")
                else:
                    ans.append("0")
            else:
                if N & (-N) == -now:
                    N -= now
                    ans.append("1")
                else:
                    ans.append("0")
            now *= (-2)

        return "".join(ans[::-1]) if ans else "0"
```

