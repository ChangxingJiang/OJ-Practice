# LeetCode题解(0507)：判断整数是否为完美数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/perfect-number/)（简单）

题目标签：

| 解法           | 时间复杂度    | 空间复杂度 | 执行用时       |
| -------------- | ------------- | ---------- | -------------- |
| Ans 1 (Python) | --            | --         | 9700ms (5.89%) |
| Ans 2 (Python) | $O(\sqrt{n})$ | O(1)       | 44ms (82.02%)  |
| Ans 3 (Python) |               |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（分解质因子，再由质因子组合因子）：

```python
def checkPerfectNumber(self, num: int) -> bool:
    # 分解质因子
    factors = [1]
    factor = 2
    temp = num
    while temp >= 0 and factor <= temp:
        if temp % factor == 0:
            factors.append(factor)
            temp //= factor
        else:
            factor += 1
        if temp == num  and factor > pow(num, 0.5) + 1:
            break

    print(factors)

    # 统计所有因子
    all_factors = [1] + factors
    for i in range(2, len(factors)):
        for group in itertools.combinations(factors, i):
            factor = 1
            for g in group:
                factor *= g
            all_factors.append(factor)

    all_factors = set(all_factors)
    if num in all_factors:
        all_factors.remove(num)

    return sum(all_factors) == num
```

解法二（枚举因数）：

```python
def checkPerfectNumber(self, num: int) -> bool:
    if num <= 1:
        return False
    factors = [1]
    for i in range(2, int(pow(num, 0.5) + 1)):
        if num % i == 0:
            factors.append(i)
            factors.append(num / i)
    return sum(factors) == num
```