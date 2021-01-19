# LeetCode题解(0858)：镜面反射(Python)

题目：[原题链接](https://leetcode-cn.com/problems/mirror-reflection/)（中等）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 40ms (49.40%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = math.gcd(p, q)
        p //= g
        q //= g

        if p % 2 == 1 and q % 2 == 1:
            return 1

        if p % 2 == 0 and q % 2 == 1:
            return 2

        return 0
```

