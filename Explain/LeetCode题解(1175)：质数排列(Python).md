# LeetCode题解(1175)：质数排列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/prime-arrangements/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (57.83%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 40ms (83.48%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def numPrimeArrangements(self, n: int) -> int:
    def countPrimes(k: int) -> int:
        if k < 2:
            return 0

        num_list = [True] * k
        num_list[0], num_list[1] = False, False

        for i in range(2, int(pow(k, 0.5)) + 1):
            if num_list[i]:
                num_list[i * i::i] = [False] * ((k - i * i - 1) // i + 1)

        return sum(num_list)

    prime_num = countPrimes(n + 1)
    other_num = n - prime_num

    ans = 1
    for i in range(1, prime_num + 1):
        ans *= i
        ans = ans % (10 ** 9 + 7)
    for i in range(1, other_num + 1):
        ans *= i
        ans = ans % (10 ** 9 + 7)
    return ans
```

解法二（不但维护了质数表，还二分查找...）：

```python
def numPrimeArrangements(self, n: int) -> int:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    prime_num = bisect.bisect_left(primes, n)
    other_num = n - prime_num
    ans = 1
    for i in range(1, prime_num + 1):
        ans *= i
        ans = ans % (10 ** 9 + 7)
    for i in range(1, other_num + 1):
        ans *= i
        ans = ans % (10 ** 9 + 7)
    return ans
```

