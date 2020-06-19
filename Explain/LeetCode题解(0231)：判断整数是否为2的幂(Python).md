# LeetCode题解(0231)：判断整数是否为2的幂(Python)

题目：[原题链接](https://leetcode-cn.com/problems/power-of-two/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | O(log(n))  | O(1)       | 36ms (>93.59%) |
| Ans 2 (Python) | O(log(n))  | O(1)       | 60ms (>10.84%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（通过除法检查是否有余数实现）：

```python
def isPowerOfTwo(self, n: int) -> bool:
    if n <= 0:
        return False
    while n > 1:
        if n % 2 != 0:
            return False
        n /= 2
    else:
        return True
```

解法二（通过乘法检查是否相等实现）：

```python
def isPowerOfTwo(self, n: int) -> bool:
    m = 1
    while m <= n:
        if m == n:
            return True
        m *= 2
    else:
        return False
```