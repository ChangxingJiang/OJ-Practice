# LeetCode题解(0625)：最小因式分解(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-factorization/)（中等）

标签：数学、递归、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 44ms (44.25%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def smallestFactorization(self, a: int) -> int:
        if a < 10:
            return a

        # 因式分解
        factors = []
        while a > 1:
            for i in range(2, 9):
                if a % i == 0:
                    a //= i
                    factors.append(i)
                    break
            else:
                return 0

        # print(factors)

        # 贪心算法合并因子
        n2, n3 = factors.count(2), factors.count(3)
        n4, n6, n8, n9 = 0, 0, 0, 0
        # 处理整除的情况
        n8, n2 = divmod(n2, 3)
        n9, n3 = divmod(n3, 2)
        if n2 >= 1 and n3 >= 1:
            n6 += 1
            n2 -= 1
            n3 -= 1
        n4, n2 = divmod(n2, 2)

        factors = ([n for n in factors if n != 2 and n != 3] +
                   [2] * n2 + [3] * n3 + [4] * n4 + [6] * n6 + [8] * n8 + [9] * n9)
        factors.sort()

        ans = int("".join([str(n) for n in factors]))

        return ans if ans < (2 ** 31) else 0
```