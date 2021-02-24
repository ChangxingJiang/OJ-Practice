# LeetCode题解(1390)：四因数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/four-divisors/)（中等）

标签：数学

| 解法           | 时间复杂度     | 空间复杂度 | 执行用时        |
| -------------- | -------------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N\sqrt{K})$ | $O(1)$     | 1456ms (16.05%) |
| Ans 2 (Python) |                |            |                 |
| Ans 3 (Python) |                |            |                 |

解法一：

```python
def factors(n):
    res = []
    k = 1
    while k * k < n:
        if n % k == 0:
            res.append(k)
            res.append(n // k)
        k += 1
    if k * k == n:
        res.append(k)
    return res


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            f = factors(num)
            if len(f) == 4:
                ans += sum(f)
        return ans
```

