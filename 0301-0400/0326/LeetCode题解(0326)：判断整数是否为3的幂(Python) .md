# LeetCode题解(0326)：判断整数是否为3的幂(Python)

题目：[原题链接](https://leetcode-cn.com/problems/power-of-three/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | O(logn)    | O(1)       | 108ms (38.66%) |
| Ans 2 (Python) | --         | O(1)       | 80ms (93.90%)  |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def isPowerOfThree(self, n: int) -> bool:
    if n<=0:
        return False
    while n > 1:
        if n % 3 != 0:
            return False
        else:
            n /= 3
    else:
        return True
```

解法二（对数运算法）：

```python
def isPowerOfThree(self, n: int) -> bool:
    if n <= 0:
        return False
    else:
        return (math.log10(n) / math.log10(3)) % 1 == 0
```