# LeetCode题解(0258)：求整数各位相加的最终得数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/add-digits/)（简单）

| 解法           | 执行用时      |
| -------------- | ------------- |
| Ans 1 (Python) | 44ms (65.86%) |
| Ans 2 (Python) | 44ms (65.86%) |
| Ans 3 (Python) | 36ms (94.40%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（转换为字符串实现）：

```python
def addDigits(self, num: int) -> int:
    while num >= 10:
        ans = 0
        for c in str(num):
            ans += int(c)
        num = ans
    return num
```

解法二（数学运算实现）：

```python
def addDigits(self, num: int) -> int:
    while num >= 10:
        ans = 0
        while num > 0:
            ans += num % 10
            num //= 10
        num = ans
    return num
```

解法三（数学方法）：

```python
def addDigits(self, num: int) -> int:
    if num == 0:
        return 0
    else:
        return (num - 1) % 9 + 1
```