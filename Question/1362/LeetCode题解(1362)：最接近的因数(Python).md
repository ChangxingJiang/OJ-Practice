# LeetCode题解(1362)：最接近的因数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/closest-divisors/)（中等）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(logN)$  | $O(logN)$  | 448ms (12.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield [k, n // k]
        k += 1
    if k * k == n:
        yield [k, k]


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        res1 = min(factors(num + 1), key=lambda x: abs(x[1] - x[0]))
        res2 = min(factors(num + 2), key=lambda x: abs(x[1] - x[0]))
        return min(res1, res2, key=lambda x: abs(x[1] - x[0]))
```

