# LeetCode题解(1071)：字符串的最大公因子(Python)

题目：[原题链接](https://leetcode-cn.com/problems/greatest-common-divisor-of-strings/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (75.64%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 36ms (92.55%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def gcdOfStrings(self, str1: str, str2: str) -> str:
    size1 = len(str1)
    size2 = len(str2)
    size = min(size1, size2)
    for i in range(size, 0, -1):
        k1 = size1 / i
        k2 = size2 / i
        if k1 % 1 == 0 or k2 % 1 == 0:
            if str1[:i] * int(k1) == str1 and str1[:i] * int(k2) == str2:
                return str1[:i]
    else:
        return ""
```

解法二：

> **【思路】**
>
> 如果存在最大公因字符串，那么str1和str2一定都是最大公约字符串的整数倍，那么str1+str2一定等于str2+str1，所以我们可以通过判断str1+str2是否等于str2+str1来判断是否存在最大公约字符串。
>
> 如果存在最大公约字符串，那么如果循环周期小于两字符串长度的最大公约数，那么长度两字符串长度的最大公约数的字符串也一定是一个循环周期，且是最大的循环周期，因此直接返回长尾两字符串长度最大公约数的字符串即可。

```python
def gcdOfStrings(self, str1: str, str2: str) -> str:
    size = math.gcd(len(str1), len(str2))
    if str1 + str2 == str2 + str1:
        return str1[: size]
    return ""
```