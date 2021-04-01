# LeetCode题解(1735)：生成乘积数组的方案数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-ways-to-make-array-with-product/)（困难）

标签：数学

| 解法           | 时间复杂度       | 空间复杂度   | 执行用时       |
| -------------- | ---------------- | ------------ | -------------- |
| Ans 1 (Python) | $O(10000+QlogN)$ | $O(10000+Q)$ | 224ms (90.31%) |
| Ans 2 (Python) |                  |              |                |
| Ans 3 (Python) |                  |              |                |

解法一：

```python
# 求n以下的质数
def get_primes(n: int) -> list:
    if n < 2:
        return []

    num_list = [True] * n
    num_list[0], num_list[1] = False, False

    for i in range(2, int(pow(n, 0.5)) + 1):
        if num_list[i]:  # 如果i为质数(不是任何质数的倍数)
            num_list[i * i::i] = [False] * ((n - i * i - 1) // i + 1)  # 因为要包含i*i所以需要+1；因为n不在列表里，所以需要-1

    return [i for i in range(n) if num_list[i]]


# 分解质因子（小于等于10000）
primes = get_primes(101)


def get_prime_factors(x):
    res = []
    for prime in primes:
        if prime > x:
            break
        while x % prime == 0:
            res.append(prime)
            x //= prime

    if x > 1:
        res.append(x)

    return res


class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        return [self.count(n, k) for n, k in queries]

    def count(self, n, k):
        """计算方案数"""
        # 处理n为1的情况
        if n == 1:
            return 1

        # 处理k为1的情况
        if k == 1:
            return 1

        # ----- 下面处理n>1且k>1的情况 -----

        # 计算k的所有因子
        factors = get_prime_factors(k)

        # 处理k只有1个质因子（自己）的情况
        if len(factors) == 1:
            return n

        # ----- 下面处理n>1且k>1且k不只1个质因子的情况 -----
        # 此时分别考虑每个质因子的分配方案数，再将各个质因子的分配方案数相乘
        # 相当于将l个小球（相同质因子的小球相同）放到n个不同的箱子中的方法
        # 使用重复组合公式
        res = 1

        factors_count = collections.Counter(factors)
        for factor, num in factors_count.items():
            res *= comb(num + n - 1, n - 1)  # 最多乘num个，num≤14

        return res % _MOD
```

