# LeetCode题解(0342)：判断整数是否为4的幂(Python)

题目：[原题链接](https://leetcode-cn.com/problems/power-of-four/)（简单）

是题目0326的延伸。

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(logn)    | O(1)       | 36ms (90.79%) |
| Ans 2 (Python) | --         | O(1)       | 36ms (90.79%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def isPowerOfFour(self, num: int) -> bool:
    if num <= 0:
        return False
    while num > 1:
        if num % 4 == 0:
            num /= 4
        else:
            return False
    else:
        return True
```

解法二（对数运算法）：

```python
def isPowerOfFour(self, num: int) -> bool:
    if num <= 0:
        return False
    else:
        return (math.log10(num) / math.log10(4)) % 1 == 0
```