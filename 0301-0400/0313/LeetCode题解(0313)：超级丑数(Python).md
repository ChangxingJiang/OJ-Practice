# LeetCode题解(0313)：超级丑数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/super-ugly-number/)（中等）

标签：数学、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N×P)$   | $O(N+P)$   | 524ms (93.96%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（多指针）：

```python
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        size = len(primes)
        idx = [0] * size  # 当前查找坐标列表
        lst = [1]

        for i in range(n - 1):
            min_idx, min_val = [], float("inf")
            for j in range(size):
                val = lst[idx[j]] * primes[j]
                if val < min_val:
                    min_idx, min_val = [j], val
                elif val == min_val:
                    min_idx.append(j)

            for j in min_idx:
                idx[j] += 1
            lst.append(min_val)

        return lst[-1]
```