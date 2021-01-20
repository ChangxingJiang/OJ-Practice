# LeetCode题解(1201)：丑数III(Python)

题目：[原题链接](https://leetcode-cn.com/problems/ugly-number-iii/)（中等）

标签：数学、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logW)$  | $O(1)$     | 44ms (29.27%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        left, right = 0, 2 * 10 ** 9

        v1 = (a * b) // math.gcd(a, b)
        v2 = (b * c) // math.gcd(b, c)
        v3 = (a * c) // math.gcd(a, c)
        v4 = (v1 * c) // math.gcd(v1, c)

        while left < right:
            mid = (left + right) // 2

            n1 = mid // a
            n2 = mid // b
            n3 = mid // c
            n4 = mid // v1
            n5 = mid // v2
            n6 = mid // v3
            n7 = mid // v4
            num = n1 + n2 + n3 - n4 - n5 - n6 + n7

            if num < n:
                left = mid + 1
            else:
                right = mid

        return left
```

